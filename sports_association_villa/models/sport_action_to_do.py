from odoo import fields, models, api, Command

class SportActionToDo(models.Model):
    _name = 'sport.action.to.do'
    _description = 'Sport Action To Do'

    name = fields.Char('Name', required=True)
    sport_issue_id = fields.Many2one('sport.issue', string='Issue')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done'),
    ], string='State', default='draft')
