# Copyright NuoBiT Solutions - Kilian Niubo <kniubo@nuobit.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

from odoo import fields, models


class SportLicense(models.Model):
    _name = "sport.license"
    _description = "Sport License"

    name = fields.Char(
        required=True,
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
    )
    start_date = fields.Date()
    end_date = fields.Date()
