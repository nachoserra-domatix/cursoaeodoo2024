# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportIssueTag(models.Model):
    _name ='sport.issue.tag'
    _description = 'Sport Issue Tag'
    
    name = fields.Char(string='Name', required=True, translate=True)
    color = fields.Integer('Color', default=0)
    sequence = fields.Integer('Sequence', default=10)