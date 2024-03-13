# Copyright NuoBiT Solutions - Kilian Niubo <kniubo@nuobit.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)
from odoo import fields, models


class SportSport(models.Model):
    _name = "sport.sport"
    _description = "Sport Sport"

    name = fields.Char(
        required=True,
    )
    description = fields.Char()
