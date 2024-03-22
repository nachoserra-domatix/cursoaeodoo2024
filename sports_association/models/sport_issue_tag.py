# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class SportIssueTag(models.Model):
    _name = "sport.issue.tag"
    _description = "Sport Issue Tag"

    # === FIELDS ===#

    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color")
