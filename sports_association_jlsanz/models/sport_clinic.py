from odoo import models, fields

class SportClinic(models.Model):
    _name = 'sport.clinic'
    _description = 'Sport Clinic'

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="phone")
    email = fields.Char('email')
    issue_ids = fields.One2many('sport.issue', 'clinic_ids', string="Issues")
    available = fields.Boolean('Available')

    def action_check_assistance(self):
        for record in self.issue_ids:
            record.assistance = True
