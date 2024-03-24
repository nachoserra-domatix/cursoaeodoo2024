# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api, Command, _
from odoo.exceptions import ValidationError

class SportIssue(models.Model):
    _name ='sport.issue'
    _description = 'Description'
    _inherit = ["portal.mixin", "mail.thread", "mail.activity.mixin"]

    name = fields.Char(string='Name', required=True,)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date', default=fields.Date.today)
    assistance = fields.Boolean(string='Assistance',help='Show if the issue has assistance')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done'),],
        string='State',
        default='draft',
        tracking=True
    )
    
    color = fields.Integer('color', default=0)    
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user, domain="[('share', '=', False)]")
    sequence = fields.Integer('Sequence', default=10)
    solution = fields.Html('Solution')
    cost = fields.Float('Cost')
    player_id = fields.Many2one('sport.player', string='Player')
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')
    tag_ids = fields.Many2many('sport.issue.tag', string='Tags')
    user_phone = fields.Char('User phone')
    assigned = fields.Boolean('Assigned', compute='_compute_assigned', inverse='_inverse_assigned')
    
    action_ids = fields.One2many('sport.actionstodo', 'issue_id', string='actions')

    _sql_constraints = [
            ('name_unique', 'unique (name)', "The issue must be unique, this one is already created."),
        ]
    
    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    # cambiamos el estado a las selecionadas a open
    # def action_open(self):
    #     self.write({'state':'open'})

    def _inverse_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id = self.env.user

    def _search_assigned(self, operator, value):
        if operator == '=':
            return [('user_id', operator, value)]
        else:
            return []

    @api.onchange('user_id')
    def _onchange_user_id(self):
        if self.user_id:
            self.user_phone = self.user_id.phone
        else:
            self.user_phone = False

    def action_open(self):
        for record in self:
            record.state = 'open'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_done(self):
        for record in self:
            record.state = 'done'
            
            
    def action_add_tags(self):
            for record in self:
                tag_ids = self.env['sport.issue.tag'].search([('name', 'ilike', record.name)])
                if tag_ids:
                    record.tag_ids = [Command.set(tag_ids.ids)]
                    #record.tag_ids = [(6, 0, tag_ids.ids)]
                else:
                    record.tag_ids = [Command.create({'name': record.name})]
                    #record.tag_ids = [(0, 0, {'name' : record.name})]

    @api.constrains('cost')
    def _verify_cost(self):
        for record in self:
            if record.cost < 0:
                raise ValidationError(_("The Cost must be a Positive."))        

    @api.onchange('clinic_id')
    def _onchange_clinic(self):
        for record in self:
            if record.clinic_id:
                record.assistance = True
            else:
                record.assistance = False
                
    def _cron_unlink_unnused_tags(self):
        tag_ids = self.env['sport.issue.tag'].search([])
        for tag in tag_ids:
            issue = self.env['sport.issue'].search([('tag_ids', 'in', tag.id)])
            if not issue:
                tag.unlink()

