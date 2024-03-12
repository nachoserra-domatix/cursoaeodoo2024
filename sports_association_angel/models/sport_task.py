from odoo import fields,models

class SportTask(models.Model):
    _name = 'sport.task'
    _description = 'Sport Task'

    name = fields.Char(string='Name', required=True)
    state = fields.Char(string='State', required=True)
    issue_id = fields.Many2one('sport.issue', string='Issue')
    # state = fields.Selection(['draft', 'open', 'done'], string='State', default='draft')

