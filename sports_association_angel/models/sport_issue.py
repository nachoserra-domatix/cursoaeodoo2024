from odoo import models, fields, api, Command, _ 
from odoo.exceptions import ValidationError, UserError

class SportIssue(models.Model):
    _name =  'sport.issue'
    _description = 'Sport Issue'

    # def _get_default_user(self):
    #    return self.env.user

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date',required=True, default=fields.Date.today)
    assistance = fields.Boolean(string='Assistance',help='Show if the issue had external assistance (paramedics)')
    state = fields.Selection(
        [('draft','Draft'),
         ('open','Open'),
         ('done','Done')],
         string='State',
         default='draft',
    )

    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)
    sequence = fields.Integer(string='Sequence', default=10)
    solution = fields.Html(string='Solution')

    clinic_id = fields.Many2one('sport.clinic', string='Clinic')   

    tags_ids = fields.Many2many('sport.issue.tag', string='Tags')
    color = fields.Integer(string="Color",default=0)
    cost =fields.Float(string="Cost", default=0.0)

    assigned = fields.Boolean(name="Assigned", compute="_compute_assigned", inverse="_inverse_assigned", search="_search_assigned",store=True)
    user_phone = fields.Char(string='User Phone')  

    task_ids = fields.One2many('sport.task', 'issue_id', string='Tasks')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', _('The name must be unique'))
    ]

    @api.constrains('cost')
    def _check_cost(self):
        for record in self:
            if record.cost < 0:
                raise ValidationError(_('The cost must be positive'))
            
    @api.onchange('clinic_id')
    def _onchange_clinic(self):
        for record in self:
            if self.clinic_id:
                self.assistance = True
            else:
                self.assistance = False

    @api.onchange('user_id')
    def _onchange_user_id(self):
        if self.user_id:
            self.user_phone = self.user_id.phone
        else:
            self.user_phone = False

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            # import pdb;pdb.set_trace()
            record.assigned = bool(record.user_id)

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

    def action_find_tags(self):
        for record in self:
            if record.name:
                tag_ids = self.env['sport.issue.tag'].search([('name','ilike',record.name)])
                if tag_ids:
                    record.tags_ids = [(6, 0, tag_ids.ids)]
                else:
                    record.tags_ids = [Command.create({'name': record.name})]
                    record.tags_ids = [(0, 0, {'name':record.name})]


    def action_open(self):
        # import pdb;pdb.set_trace()

        # self.ensure_one()
        for record in self:
            record.state = 'open'
        # self.write({'state': 'open'})
    
    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_done(self):
        for record in self:
            if not record.date:
                raise UserError(_("The date is required"))
            else:
                record.state = 'done'
            
    def action_open_all_issues(self):
        issues = self.env['sport.issue'].search([])
        issues.action_open()

    def _cron_unlink_unused_tags(self):
        tags_ids = self.env['sport.issue.tag'].search([])
        for tag in tags_ids:
            issue = self.env['sport.issue'].search([('tags_ids','in',tag.id)])
            if not issue:
                tag.unlink()
