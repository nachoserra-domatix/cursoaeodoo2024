# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class SportLicense(models.Model):
    _name = "sport.license"
    _description = "Sport License"

    # === FIELDS ===#

    name = fields.Char(string="name", required=True)
    partner_id = fields.Many2one(comodel_name="res.partner")
    start_date = fields.Datetime(
        required=True,
        default=fields.Datetime.now,
        help="Start date.",
    )
    end_date = fields.Datetime(
        required=True,
        default=fields.Datetime.now,
        help="Issue date.",
    )
    reference = fields.Char(string="Reference")
