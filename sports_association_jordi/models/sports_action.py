from odoo import models, fields

class SportsAction(models.Model):
    _name = 'sports.action'
    _description = 'Sports Action'

    name = fields.Char(string='Name')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done')
    ], string='State', default='draft')
    issue_id = fields.Many2one('sports.issue', string='Issue')