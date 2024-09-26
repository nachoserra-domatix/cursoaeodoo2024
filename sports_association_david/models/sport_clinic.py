from odoo import models, fields

class SportClinic(models.Model):
    _name = 'sport.clinic'
    _description = 'Sport Clinic'

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="phone")
    email = fields.Char(string="Mail")

    issue_ids = fields.One2many('sport.issue', 'clinic_id')
    
    available = fields.Boolean(string="Available")

    def action_check_assistance(self):
        self.issue_ids.write({'assistance' : True})