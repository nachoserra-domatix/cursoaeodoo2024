# Copyright NuoBiT Solutions - Kilian Niubo <kniubo@nuobit.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)
from odoo import fields, models


class SportClinic(models.Model):
    _name = "sport.clinic"
    _description = "Sport Clinic"

    name = fields.Char(
        required=True,
    )
    phone = fields.Char()
    email = fields.Char()
    issue_ids = fields.One2many(
        comodel_name="sport.issue",
        inverse_name="clinic_id",
    )

    def action_check_assistance(self):
        for rec in self.issue_ids:
            rec.assistance = True
