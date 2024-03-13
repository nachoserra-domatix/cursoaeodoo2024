from odoo import models, fields, api, Command, _
from odoo.exceptions import ValidationError
from datetime import datetime

class SportIssue(models.Model):

    _name = 'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    date = fields.Date(string='Date', default=datetime.now())
    state = fields.Selection(string='State', selection=[('draft','Draft'),('open','Open'),('done','Done')], default='draft')
    assistance = fields.Boolean(string='Assistance')
    user_id = fields.Many2one(string='Usuario', comodel_name='res.users', default=lambda self:self.env.user)
    user_phone = fields.Char(string='Phone')
    sequence = fields.Integer(string='Sequence')
    solution = fields.Html(string='Solution')
    tag_ids = fields.Many2many('sport.tag', string='Tag')
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')
    color = fields.Integer(string='Color', default=0)
    action_ids = fields.One2many('sport.action', 'issue_id', string='Actions')
    cost = fields.Float('Cost')
    assigned = fields.Boolean('Assigned', compute='_compute_assigned', inverse='_inverse_asigned', search='_search_asigned', store=False)
    player_id = fields.Many2one('sport.player', string='Player')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "The Name must be unique, this one is already assigned to another Issue.")
    ]

    @api.constrains('cost')
    def verify_cost(self):
        for rec in self:
            if rec.cost < 0:
                raise ValidationError(_("The cost must be positive."))
    
    @api.onchange('clinic_id')
    def _on_change_clinic(self):
        for rec in self:
            if rec.clinic_id:
                rec.assistance = True

    @api.onchange('user_id')
    def _on_change_user(self):
        for rec in self:
            if rec.user_id and rec.user_id.partner_id.phone:
                rec.user_phone = rec.user_id.partner_id.phone
            else:
                rec.user_phone = False
    
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    @api.depends('user_ids')
    def _inverse_asigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id = self.env.user

    def _search_asigned(self, operator, value):
        if operator == '=':
            return [('user_id','=',value)]
        else:
            return []

    def action_open(self):
        for record in self:
            record.write({
                'state': 'open'
            })
    def action_draft(self):
        for record in self:
            record.write({
                'state': 'draft'
            })
    def action_done(self):
        for record in self:
            record.write({
                'state': 'done'
            })

    def action_open_all_issues(self):
        issues= self.env['sport.issue'].search([])
        issues.action_open()

    def assign_tags(self):
        for record in self:
            tag_ids = self.env['sport.tag'].search([('name', 'like', self.name)]).ids
            if not tag_ids:
                self.write({
                    # 'tag_ids': [(0,0,{'name': self.name})]
                    'tag_ids': [Command.create({'name': self.name})]
                })
            else:
                self.write({
                    'tag_ids': [Command.set(tag_ids)]
                })
