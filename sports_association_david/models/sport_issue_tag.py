from odoo import models, fields

class SportIssueTag(models.Model):
    _name = 'sport.issue.tag'

    name = fields.Char(string="Name", required=True)

    issue_ids = fields.Many2many('sport.issue', string='Sport Issue')