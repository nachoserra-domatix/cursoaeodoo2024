from odoo import models, fields

class SportClinic(models.Model):
    _name = 'sport.clinic'
    _description = 'Sport Clinic'

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="phone")
    email = fields.Char('email')
    issue_ids = fields.One2many('sport.issue', 'clinic_ids', string="Issues")
    available = fields.Boolean('Available')
    issue_count = fields.Integer('Issue count', compute='_compute_issue_count')

    def _compute_issue_count(self):
        for record in self:
            record.issue_count = len(record.issue_ids)

    def action_check_assistance(self):
        for record in self.issue_ids:
            record.assistance = True

    # Smart button
    def action_view_issues(self):
        return {
            'name': 'Issues',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.issue',
            'view_mode': 'tree,form',
            'domain': [('clinic_ids', '=', self.id)],
        }