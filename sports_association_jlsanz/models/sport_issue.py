from odoo import models, fields

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char(string='Name')
    description = fields.Text(string='Desciption')
    date = fields.Date(string='Date')
    assistance = fields.Boolean(string='Assistance', help="Show")
    state = fields.Selection(
        [('draft', 'Draft'),
         ('open', 'Open'),
         ('done', 'Done')],
        string='State',
        default='draft'
    )

    user_id = fields.Many2one('res.users', string="User")
    sequence = fields.Integer(string="Sequence", default="10")
    solution = fields.Html(string="Solutions")
