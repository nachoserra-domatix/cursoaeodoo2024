# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields

class SportCreateIssue(models.TransientModel):
    _name ='sport.create.issue'
    _description = 'Description'
    
    name = fields.Char(string='IssueName', required=True,)
    clinic_id = fields.Many2one(comodel_name='sport.clinic', string='Clinic', default=lambda self: self.env.context.get('active_id'))

    def create_issue(self):
        vals = {
            'name': self.name,
            'clinic_id': self.clinic_id.id
            }
        self.env['sport.issue'].create(vals)
    