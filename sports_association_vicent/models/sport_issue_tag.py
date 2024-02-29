# Copyright 2024 Vicent Esteve - vesteve@ontinet.com
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class SportIssueTag(models.Model):
    _name = 'sport.issue.tag'
    _description = "Sport Issue Tag"

    name = fields.Char(string='Name', required=True)
    