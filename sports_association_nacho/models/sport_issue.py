from odoo import models, fields

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char(string="Name", required=True),
    description = fields.Text(string="Description"),
    date = fields.Date(string="Date"),
    assistance = fields.Boolean(string="Assistance", help="Show if the issu has assistance"),
    state = fields.Selection(
        [('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done'),],
        string = 'State',
        default = 'draft',
    ),
