# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = "sport issue"

    name = fields.Char(string="name")
    description = fields.Text(string="Description")
    date = fields.Datetime(
        readonly=True,
        required=True,
        string="Date",
        default=fields.Datetime.now,        
        help="Issue date.",
    )
    assistance = fields.Boolean(string="Assistance")
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("open", "Open"),
            ("done", "Done"),
            ("expired", "Expired"),
        ],
        string="State",
        default="draft",
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string="User",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=10, 
    )
    solution = fields.Html(string="Solution")
    