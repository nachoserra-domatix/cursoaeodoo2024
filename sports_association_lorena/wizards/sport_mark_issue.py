from odoo import models, fields

class SportMarkIssue(models.TransientModel):
    _name = 'sport.mark.issue'
    _description = 'Mark Issue'

    name = fields.Char('Name')
    issue_id = fields.Many2one('Issue')

    def mark_done(self):
        issues = self.env['sport.issue'].search([])
        issues.write({'state': 'done'})