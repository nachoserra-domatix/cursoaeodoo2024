# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields

SPORT_ISSUE_STATE = [
    ('draft', "Draft"),
    ('open', "Open"),
    ('done', "Done"),
    ('expired', "Expired"),
]

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = "sport issue"

    #=== FIELDS ===#

    name = fields.Char(string="name")
    description = fields.Text(string="Description")
    date = fields.Datetime(
        readonly=True,
        required=True,
        string="Date",
        default=fields.Datetime.now,        
        help="Issue date")
    assistance = fields.Boolean(string="Assistance")
    state = fields.Selection(
        selection=SPORT_ISSUE_STATE,
        string="Status",
        default="draft")
    user_id = fields.Many2one(
        comodel_name='sport.player',
        string="User")
    sequence = fields.Integer(
        string="Sequence",
        default=10)
    solution = fields.Html(string="Solution")

    clinic_id = fields.Many2one(
        comodel_name="sport.clinic", 
        string="Clinic")
    tag_ids = fields.Many2many(
        comodel_name="sport.issue.tag", 
        string="Tag")
    cost = fields.Integer(string="Cost")

    #=== METHODS ===#

    def action_draft (self):
        self.state='draft'
    
    def action_open (self):
        self.write({'state':'open'})

    def action_close (self):
        self.state='done'
    