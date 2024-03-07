# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SportIssueAction(models.Model):
    _name = 'sport.issue.action'
    _description = 'Sport Issue Action'

    name = fields.Char(string='Name', required=True)
    issue_id = fields.Many2one('sport.issue', string='Issue')
    state = fields.Selection(
        [('draft', 'Draft'),
         ('open', 'Open'),
         ('done', 'Done')],
        string='State',
    )