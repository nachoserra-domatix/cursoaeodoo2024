from odoo import fields, models, Command, api
from odoo.exceptions import ValidationError

import datetime

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sports Issues'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    date = fields.Date(string="Date", default=fields.Date.today)
    assistance = fields.Boolean(string="Assistance")
    state = fields.Selection(
        [('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done')
        ],
        string="State",
        default='draft'
    )
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)
    player_id = fields.Many2one(string='Player', comodel_name='sport.player')
    phone_user = fields.Char("User Phone", readonly=True)
    secuence = fields.Integer(string='secuence', default=10)
    solution = fields.Html(string="Solution")
    clinic_id = fields.Many2one(
        string='Clinic',
        comodel_name='sport.clinic',
    )
    tag_ids = fields.Many2many(
        string='Tags',
        comodel_name='sport.issue.tag',
    )
    color = fields.Integer(string="Color", default=0)
    cost = fields.Float(string="Cost")
    assigned = fields.Boolean(string="Assigned", compute="_compute_assigned", readonly=True)
    actions_ids = fields.One2many(string="Actions To Do", comodel_name='sport.issue.action', inverse_name='issue_id',)

    _sql_constraints = [
        ('name_unique', 'unique (name)', "The issue name must be unique!"),
    ]
    

    @api.constrains('cost')
    def _check_cost(self):
        for record in self:
            if record.cost < 0:
                raise ValidationError("The cost must be positive")

    @api.onchange('clinic_id')
    def _onchange_clinic_id(self):
        for record in self:
            if record.clinic_id:
                record.assistance = True
            else:
                record.assistance = False

    @api.onchange('user_id')
    def _onchange_user_id(self):
        for record in self:
            if record.user_id:
                record.phone_user = record.user_id.phone
            else:
                record.phone_user = False

    def _compute_assigned(self):
        self.assigned = False
        if self.user_id:
            self.assigned = True
    
    def action_open(self):
        for record in self:
            record.state = 'open'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_tags(self):
        for record in self:
            existing_tag_ids = self.env['sport.issue.tag'].search([('name', 'like', record.name)])
            if len(existing_tag_ids):
                record.tag_ids = [Command.set(existing_tag_ids.ids)]
            else:
                record.tag_ids = [Command.create({'name': record.name})]
