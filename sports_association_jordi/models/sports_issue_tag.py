from odoo import models, fields

class SportsIssueTag(models.Model):
    _name = 'sports.issue.tag'
    _description = 'Sports Issue Tag'

    name = fields.Char(string='Name',required=True)