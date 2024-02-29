from odoo import models, fields


class SportClinic(models.Model):
    _name = "sport.clinic"
    _description = "Sport Clinic"

    name = fields.Char(string='Name', required=True)
    phone = fields.Char('Phone')
    email = fields.Char('Email')
    issue_ids = fields.One2many('sport.issue', 'clinic_id', string='Issues')

    def action_check_assistance(self):
        for record in self.issue_ids:
            record.assistance = True
    