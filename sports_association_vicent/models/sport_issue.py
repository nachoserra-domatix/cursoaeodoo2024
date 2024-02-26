# Copyright 2024 Vicent Esteve - vesteve@ontinet.com
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = "Sport Issue"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    assistance = fields.Boolean(string='Assistante', help='Show if the isuue has asssitence')
    state = fields.Selection([
        ('dradt', 'Draft'),
        ('open', 'Open'),
        ('draft', 'Done')],
        string='Assistante',
        default='draft',
    )
