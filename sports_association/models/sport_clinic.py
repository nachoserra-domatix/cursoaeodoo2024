# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportCLinic(models.Model):
    _name ='sport.clinic'
    _description = 'Sport Clinic'
    
    name = fields.Char(string='Name', required=True)
    phone = fields.Char('phone')
    email = fields.Char('email')
    issue_ids = fields.One2many('sport.issue', 'clinic_id', string='Issues')
    available = fields.Boolean('available')
    issue_count = fields.Integer('Issue count', compute='_compute_issue_count')


    def _compute_issue_count(self):
        for record in self:
            record.issue_count = len(record.issue_ids)


    def action_check_assistance(self):
        for record in self.issue_ids:
            record.assistance = True

    # Smart button for issues
    def action_view_issues(self):

        return {
            'name': 'Issues',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.issue',
            'view_mode': 'tree,form',
            'domain': [('clinic_id', '=', self.id)],
        }
