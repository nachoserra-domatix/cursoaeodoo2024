from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sport Issue'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']

    def _get_default_user(self):
        return self.env.user

    name = fields.Char(string='Name')
    description = fields.Text(string='Desciption')
    date = fields.Date(string='Date', default=fields.Date.today )
    assistance = fields.Boolean(string='Assistance', help="Show")
    state = fields.Selection(
        [('draft', 'Draft'),
         ('open', 'Open'),
         ('done', 'Done')],
        string='State',
        default='draft',
        tracking=True,
    )

    user_id = fields.Many2one('res.users', string="User", default=_get_default_user)
    #user_id = fields.Many2one('res.users', string="User", default=lambda self: self.env.user)
    sequence = fields.Integer(string="Sequence", default="10")
    solution = fields.Html(string="Solutions")
    color = fields.Integer(string="Color", default=0)
    cost = fields.Float(string="cost")

    assigned = fields.Boolean(string='Assigned', compute='_compute_assigned', inverse='_inverse_assigned')

    clinic_ids= fields.Many2one('sport.clinic', string='Clinic')

    action_ids= fields.One2many('sport.issue.action', 'issue_id', string='Action')

    tag_ids = fields.Many2many('sport.issue.tag', string='Tags')

    player_id = fields.Many2one('sport.player', string='Player')

    #user_phone = fields.Char(string='User_phone', related='user_id.phone', store=True. readonly=False)
    user_phone = fields.Char(string='User_phone')

    _sql_constraints = [ ('name_uniq', 'unique (name)', "The name must be unique!"),  ]

    @api.constrains('cost')
    def _check_cost(self):
        for record in self:
            if record.cost < 0:
                raise ValidationError(_('The cost must be positive'))

    @api.onchange('user_id')
    def _onchange_user_id(self):
        if self.user_id:
            self.user_phone = self.user_id.phone
        else:
            self.user_phone = False

    @api.onchange('clinic_ids')
    def _onchange_clinic(self):
        for record in self:
            if record.clinic_ids:
                record.assistance = True
            else:
                record.assistance = False

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    def _inverse_assigned(self):
            for record in self:
                if not record.assigned:
                    record.user_id = False
                else:
                    record.user_id = self.env.user

    #def _search_assigned(self):

    def action_open(self):        
        for record in self:
            record.state = 'open'

    def action_draft(self):        
        for record in self:
            record.state = 'draft'

    def action_done(self):        
        for record in self:
            if not record.date:
                raise UserError(_('The date is required'))
            record.state = 'done'
            # Al heredar mixin
            msg_body = f'La incidencia ha pasado al estado {record.state} con fecha {record.date}'
            record.message_post(body=msg_body)

#    def action.open_all_issues(self):
#        for record in self:
#            action.open(record)

    def action_add_tags_like_name(self):
        for record in self:
                result_tags = self.env['sport.issue.tag'].search([('name', 'ilike', record.name)])
                #import pdb; pdb.trace();
                if result_tags:
                    record.tag_ids = [(6,0,result_tags.ids)]
                else:
                    record.tag_ids = [(0,0,{'name':record.name})]

    def _cron_unlink_unused_tags(self):
        tag_ids = self.env['sport.issue.tag'].search([])
        for tag in tag_ids:
            issue = self.env['sport.issue'].search([('tag_ids', 'in', tag.id)])
            if not issue:
                tag.unlink()
