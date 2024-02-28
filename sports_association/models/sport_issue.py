from odoo import fields, models

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sports Issues'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    date = fields.Date(string="Date")
    assistance = fields.Boolean(string="Assistance")
    state = fields.Selection(
        [('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done')
        ],
        string="State",
        default='draft'
    )

    user_id = fields.Many2one('res.users', string='User')
    secuence = fields.Integer(string='secuence', default=10)
    solution = fields.Html(string="Solution")