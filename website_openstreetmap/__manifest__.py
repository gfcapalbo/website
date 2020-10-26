# -*- coding: utf-8 -*-
{
    "name": "Openstreetmap Widget",
    "version": "14.0.1.0.0",
    "author": "Therp BV, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Website",
    "summary": "Replaces Google maps on website, adds OpenStreetMap widget",
    "depends": [
        'website'
    ],
    "data": [
        "views/view.xml",
        "views/widget.xml",
    ],
    "auto_install": False,
    "installable": True,
    "external_dependencies": {
        'python': [],
    },
}
