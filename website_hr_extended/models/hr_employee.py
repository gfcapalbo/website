# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    position = fields.Integer('Position in aboutus page', default=9999)
    bio_website = fields.Text('Biography (for about us page) ')
    github_website = fields.Char('Github Address (for about us page)')
    linkedin_website = fields.Char('Linkedin Address (for about us page)')
    twitter_website = fields.Char('Twitter Address (for about us page)' )

