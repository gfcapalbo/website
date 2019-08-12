# Copyright 2017 Simone Orsi
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import fields, models


class WebsiteMenu(models.Model):
    _inherit = 'website.menu'

    # TODO: when we'll have an advanced form for editing groups
    # we should add an handler to update flags (like `_update_menu_groups`)
    group_ids = fields.Many2many(
        comodel_name='res.groups',
    )
