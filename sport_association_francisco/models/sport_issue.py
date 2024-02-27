from odoo import models, fields

class SportIssue(models.Model):

    _name = 'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    state = fields.Selection(string='State', selection=[('draft','Draft'),('open','Open'),('done','Done')], default='draft')
    assistance = fields.Boolean(string='Assistance')
