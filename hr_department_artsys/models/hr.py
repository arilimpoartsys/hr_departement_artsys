# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError
from odoo.modules.module import get_module_resource
# from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as OE_DFORMAT
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_DFORMAT
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Employee(models.Model):
    _inherit = "hr.employee"

    directorate_id = fields.Many2one('hr.department', domain="[('category','=','dir')]", string='Directorate',track_visibility='onchange')
    division_id = fields.Many2one('hr.department', domain="[('category','in',('dir','div'))]", string='Division', track_visibility='onchange')
    department_id = fields.Many2one('hr.department', domain="[('category','in',('dir','div','dep'))]", string='Department', track_visibility='onchange')
    unit_id = fields.Many2one('hr.department', domain="[('category','in',('dir','div','dep','unit'))]",string='Unit', track_visibility='onchange')
    subunit_id = fields.Many2one('hr.department', domain="[('category','in',('dir','div','dep','unit','sunit'))]", string='Sub-unit', track_visibility='onchange')

