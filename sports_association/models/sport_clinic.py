# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportCLinic(models.Model):
    _name ='sport.clinic'
    _description = 'Sport Clinic'
    
    name = fields.Char(string='Name', required=True)
    phone = fields.Char('phone')
    email = fields.Char('email')
    issue_ids = fields.One2many('sport.issue', 'clinic_id', string='Issues')

    def action_check_assistance(self):
        for record in self.issue_ids:
            record.assistance = True