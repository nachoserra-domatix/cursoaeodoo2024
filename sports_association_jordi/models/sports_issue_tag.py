from odoo import models, fields

class SportsIssueTag(models.Model):
    _name = 'sports.issue.tag'
    _description = 'Sports Issue Tag'

    name = fields.Char(string='Name',required=True,translate=True)
    color = fields.Integer(string='Color Index',default=0)
    issue_ids = fields.Many2many('sports.issue', 'sports_issue_tag_rel','tag_id','issue_id',string='Issues')
