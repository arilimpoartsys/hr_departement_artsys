# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models


class Department(models.Model):
    _inherit = "hr.department"

    category = fields.Selection([
        ('dir', 'Directorate'),
        ('div', 'Division'),
        ('dep', 'Department'),
        ('unit','Unit'),
        ('sunit', 'Sub Unit'),
        ('com', 'Committee'),
        ('sec', 'Secretariat'),
    ], string='Category', track_visibility='onchange',)
    note = fields.Text(string='Note')
    active = fields.Boolean('Active', default=True)

