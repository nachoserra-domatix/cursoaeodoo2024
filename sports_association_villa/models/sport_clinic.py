from odoo import fields, models

class SportClinic(models.Model):
    _name = 'sport.clinic'
    _description = 'Sport Clinic'

    name = fields.Char('Name', required=True)
    phone = fields.Char('Phone')
    email = fields.Char('Email')
    issue_ids =  fields.One2many('sport.issue', 'clinic_id', string='Issues')

    def action_check_assistance(self):
        #import pdb; pdb.set_trace()
        self.issue_ids.write({'assistance': True})