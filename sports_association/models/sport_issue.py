# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields, Command, _
from odoo.exceptions import ValidationError

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
        string="User",
        default=lambda self: self.env.user.id)
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
    color = fields.Integer(string="Color")
    assigned = fields.Boolean('Assigned', compute='_compute_assigned', store=True)
    action_ids = fields.One2many('sport.issue.action', 'issue_id', string='Actions to do')

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)
    
    @api.constrains('cost')
    def _check_coste_no_negativo(self):
        for record in self:
            if record.cost < 0:
                raise ValidationError(_("The cost must be positive."))
            
    @api.onchange( 'clinic_id')
    def _onchange_clinic_id (self):
        self.assistance = True
    
    # def _inverse_assigned(self):
    #     for record in self:
    #         if not record.assigned:
    #             record.user_id = self.user_id;
    #         else:
    #             record.user_id = self.env.user

    def _search_assigned(self, operator, value):
        if operator == '=':
            return [('user_id', operator, value)]
        else:
            return []

    #=== METHODS ===#

    def action_draft (self):
        self.state='draft'
    
    def action_open (self):
        self.write({'state':'open'})

    def action_close (self):
        self.state='done'

    def action_add_tag(self):
        for record in self:
            tag_ids = self.env['sport.issue.tag'].search([('name', 'ilike', record.name)])
            if tag_ids:
                record.tag_ids = [Command.set(tag_ids.ids)]
                 # record.tag_ids = [(6, 0, tag_ids.ids)]
            else:
                record.tag_ids = [Command.create({'name': record.name})]
                record.tag_ids
               # record.tag_ids = [(0, 0, {'name': record.name})]
    