# -*- coding: utf-8 -*-

import urllib
import json
from odoo import models, fields, api, exceptions, _


class ResCompany(models.Model):

    _inherit = "res.company"

    gps_longitude = fields.Char('longitude gps',)
    gps_latitude = fields.Char('latitude gps',)

    def openstreetmap_img(self, zoom=16, width=250, height=250):
        url = 'http://staticmap.openstreetmap.de/staticmap.php'
        params = {
            'center': "{lat},{lon}".format(
                lat=self.gps_latitude or '',
                lon=self.gps_longitude or ''),
            'size': "%sx%s" % (height, width),
            'zoom': zoom,
            'maptype': 'mapnik',
            'map': "{zm}/{lat}/{lon}".format(
                zm=zoom,
                lat=self.gps_latitude or '',
                lon=self.gps_longitude or ''),
        }
        return url + '?%s' % urllib.urlencode(params)

    def openstreetmap_link(self, zoom=16):
        url = 'http://www.openstreetmap.org'
        params = {
            'mlat': self.gps_latitude,
            'mlon': self.gps_longitude,
            'zoom': zoom,
            'layers': 'M',
            'map': "{zm}/{lat}/{lon}".format(
                zm=zoom,
                lat=self.gps_latitude or '',
                lon=self.gps_longitude or '', )
        }
        return url + '?%s' % urllib.urlencode(params)

    def get_nominatim_openstreetmap_coordinates(self):
        url = 'http://nominatim.openstreetmap.org/search'
        params = {
            'format': 'json',
            'street': self.street or '',
            'city': self.city or '',
            'country': self.country_id.code or '',
            'postalcode': self.zip or '',
        }
        query = urllib.urlencode(params)
        req = urllib.urlopen(url+'?%s' % query)
        json_request = req.read()
        res = json.loads(json_request)
        if not res:
            raise exceptions.Warning(_(
                'No results found. Check if your '
                'address is correct: \n 1.If the street number is in the '
                'street field it may \n offset openstreetmaps\'s search. '
                'Try Removing the number.\n 2.Check if Street, zipcode, '
                'city and country are all \n compiled and correct, '
                'the search uses all four of them.\n  3.If the search still '
                'does not work, it is possible to  insert \n the GPS '
                'coordinates manually in the fields above.'))
        # todo : provide a list of selections, now taking first.
        self.write({
            'gps_longitude': res[0]['lon'],
            'gps_latitude': res[0]['lat'],
            })
        return {}
