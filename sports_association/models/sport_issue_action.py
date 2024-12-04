from odoo import models, fields


class SportIssueAction(models.Model):
    _name = 'sport.issue.action'
    _description = 'Sport Issue Action'

    name = fields.Char(string='Name')
    issue_id = fields.Many2one(comodel_name='sport.issue', string='Issue')
    state = fields.Selection(string='State', selection=[('draft', 'Draft'), ('open', 'Open'), ('done', 'Done')])
    
    issue_id = fields.Many2one(comodel_name='sport.issue', string='Issue')
    