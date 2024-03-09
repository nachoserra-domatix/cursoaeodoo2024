from odoo import fields, models

class SportIssueTag(models.Model):
    _name = 'sport.issue.tag'
    _description = 'Sport Issue Tag'

    name = fields.Char('Name', required=True)
    color = fields.Integer(string='Color', default=0)