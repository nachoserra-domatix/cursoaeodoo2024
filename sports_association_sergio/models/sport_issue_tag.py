from odoo import models, fields

class SportIssueTag(models.Model):
    _name = 'sport.issue.tag'
    _description = 'Sport Issue Tag'

    name = fields.Char(string='Name', required=True, translate=True)
    color = fields.Integer(string="Color", default=0)

