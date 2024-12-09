from odoo import models, fields, Command,api,_
from odoo.exceptions import ValidationError, UserError

class SportsIssue(models.Model):
    _name = 'sports.issue'
    _description = 'Sports Issue'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date',default=fields.Date.context_today)
    assistance = fields.Boolean(string='Assistance',help='Show if the issue has assitastance')
    state=fields.Selection(
        [('draft', 'Draft'),
          ('open', 'Open'),
          ('done','Done') ],
          string='State',
          default='draft',
          tracking=True)
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)
    sequence = fields.Integer(string='Sequence',default=10)
    solution = fields.Html(string='Solution')
    clinic_id = fields.Many2one('sports.clinic', string='Clinic')
    tag_ids = fields.Many2many('sports.issue.tag', 'sports_issue_tag_rel','issue_id','tag_id',string='Tags')
    color = fields.Integer(string='Color Index',default=0)
    cost=fields.Float(string='Cost',tracking=True)
    assigned=fields.Boolean(string="Assigned",compute='_compute_asigned',inverse='_inverse_assigned',store=True)
    action_ids = fields.One2many('sports.action','issue_id',string='Actions')
    # user_phone = fields.Char(string='User Phone',related='user_id.phone',store=True, readonly=False)
    user_phone = fields.Char(string='User Phone')

    _sql_constraints = [('name_uniq', 'unique(name)', 'The name must be unique')]

    def action_done(self):
        for record in self:
            if record.date:
                 record.state='done'
            else:
                raise UserError(_("The date is necessary"))
    
    def action_open(self):
        for record in self:
            record.state='open'
    
    def action_draft(self):
        for record in self:
            record.state='draft'

    @api.depends('user_id')   
    def _compute_asigned(self):
        for issue in self:
            issue.assigned=bool(issue.user_id)

    def _inverse_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id = self.env.user
    
    def action_add_tag(self):
        for record in self:
            tag_ids = self.env['sports.issue.tag'].search([("name", "ilike", record.name)])
            if tag_ids:
                record.tag_ids = [Command.set(tag_ids.ids)]
                #record.tag_ids = [6,0,tag_ids.ids]
            else:
                record.tag_ids = [Command.create({'name': record.name})]
            
    @api.constrains('cost')
    def _check_cost(self):
        for record in self:
            if record.cost<0:
                raise ValidationError(_('The cost must be positive'))
    
    @api.onchange('clinic_id')
    def _onchange_clinic_id(self):
        if self.clinic_id:
            self.assistance=True
        else:
            self.assistance=False
    
    @api.onchange('user_id')
    def _onchange_user_id(self):
        if self.user_id:
            self.user_phone=self.user_id.phone
        else:
            self.user_phone=False
    def _cron_delete_unused_tags(self):
        tag_ids = self.env['sports.issue.tag'].search([])
        for tag in tag_ids:
            issue = self.env['sports.issue'].search([('tag_ids', 'in', tag.id)])
            if not issue:
                tag.unlink()
