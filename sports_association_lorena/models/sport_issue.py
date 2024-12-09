from odoo import models, fields, Command, api, _
from odoo.exceptions import ValidationError
import datetime

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    date = fields.Date(string='Date', default=fields.Date.today)
    assistance = fields.Boolean(string='Assistance', help='Show if the issue has assistance')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('done', 'Done')], string='State', default='draft')
    user_id = fields.Many2one('res.users', string="User")
    sequence = fields.Integer(string="Sequence", default=10)
    solution = fields.Html(string='Solution')
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')
    tag_ids = fields.Many2many('sport.issue.tag', string='Tags')
    color = fields.Integer(string='Color', default=0)
    cost = fields.Float(string='Cost')
    assigned = fields.Boolean(string='Assigned', compute='_computed_assigned')
    actions_ids = fields.One2many('sport.action', 'issue_id', string='Actions')
    user_phone = fields.Char(string='User Phone')
    player_id = fields.Many2one('sport.player', string='Player')

    _sql_constraints = [
        ("unique_name", "UNIQUE(name)", "The name of the incidence must be unique.")
    ]
    
    @api.constrains('cost')
    def _check_cost(self):
        for record in self:
            if record.cost < 0:
                raise ValidationError(_('The cost must be positive.'))
            
    @api.onchange('user_id')
    def _onchange_(self):
        if self.user_id:
            self.user_phone = self.user_id.phone
        else:
            self.user_phone = False
            
    @api.onchange('clinic_id')
    def _onchange_clinic(self):
        for record in self:
            if record.clinic_id:
                record.assistance = True
            else:
                record.assistance = False
            
    @api.depends('user_id')
    def _computed_assigned(self):
        for record in self:
            if record.user_id:
                record.assigned = True

    def action_open(self):
        for record in self:
            record.state = 'open'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_close(self):
        for record in self:
            record.state = 'close'

    def action_add_tag(self):
        for record in self:
            # import pdb;pdb.set_trace()
            tag_ids = self.env['sport.issue.tag'].search([('name', 'ilike', record.name)])
            if tag_ids:
                record.tag_ids = [(6, 0, tag_ids.ids)]
            else:
                record.tag_ids = [Command.create({'name': record.name})]