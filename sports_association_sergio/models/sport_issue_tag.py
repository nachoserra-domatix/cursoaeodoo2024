from odoo import models, fields

class SportIssueTag(models.Model):
    _name = 'sport.issue.tag'
    _description = 'Sport Issue Tag'

    name = fields.Char(string='Name', required=True, translate=True)
    color = fields.Integer(string="Color", default=0)

def _remove_unused_tags(self):
# Remove tags that are not referenced by any issue
    self.env['sport.issue.tag'].search([
        ('id', 'not in', self.mapped('tags_ids').ids)
    ]).unlink()
