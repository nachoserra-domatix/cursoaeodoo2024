from odoo import models, fields



class SportIssueTag(models.Model):
    _name = 'sport.issue.tag'
    _description = 'Sport Issue Tag'

    name = fields.Char(string='Name', required=True)
    
