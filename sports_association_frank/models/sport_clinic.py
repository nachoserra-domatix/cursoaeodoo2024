from odoo import models, fields

class SportClinic(models.Model):
    _name = "sport.clinic"
    _description = "Sport Clinic"


    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    issue_ids = fields.One2many(
        comodel_name="sport.issue",
        inverse_name="clinic_id",
        string="Issues",
    )

    def action_check_assistance():
        for rec in self:
            rec.issue_ids.write({"state": "done"})
