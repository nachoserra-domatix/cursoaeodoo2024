# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportActionsTODO(models.Model):
    _name ='sport.actionstodo'
    _description = 'Issues Actions ToDo'

    name = fields.Char(string='Name', required=True)
    action_state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done'),],
        string='State',
        default='draft',
    )
    issue_id = fields.Many2one('sport.issue', string='issue')