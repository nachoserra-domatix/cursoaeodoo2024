from odoo import models, fields

class SportAction(models.Model):

    _name = 'sport.action'
    _description = 'Sport Action'

    name = fields.Char(string="Name")
    issue_id = fields.Many2one('sport.issue', string='Isue')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done'),
    ], string='State')
