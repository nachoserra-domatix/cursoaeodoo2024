from odoo import models, fields

class SportClinic(models.Model):

    _name = 'sport.clinic'
    _description = 'Sport Clinic'

    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    
    issue_ids = fields.One2many('sport.issue', 'clinic_id',string="Issues")

    def action_check_assistance(self):
        self.issue_ids.write({
            'assistance': True
        })