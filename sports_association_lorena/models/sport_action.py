from odoo import models, fields

class SportAction(models.Model):
    _name = 'sport.action'
    _description = 'SportAction'

    name = fields.Char(string="Nombre", required=True)
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('done', 'Done')], string='State', default='draft')
    issue_id = fields.Many2one('sport.issue', string="Issue")