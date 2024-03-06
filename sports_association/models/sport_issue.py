from odoo import models, fields, api, Command

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = "Sport Issue"
    
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    assistance = fields.Boolean(string='Assistance', help='Show if the issue has assistance')
    state = fields.Selection([
        ('draft','Draft'),
        ('open','Open'),
        ('done','Done')
        ],
        string='State',
        default='draft'
    )    

    color = fields.Integer(string="Color", default="0")
    user_id = fields.Many2one('res.users', string='User')
    sequence = fields.Integer(string='Sequence', default=10)
    solution = fields.Html('Solution')
    assigned = fields.Boolean('Assigned', compute='_compute_assigned', inverse='_inverse_assigned', search='_search_assigned', store=True)

    clinic_id = fields.Many2one('sport.clinic', string='Clinic')

    tag_ids = fields.Many2many('sport.issue.tag', string='Tags')

    to_do_action_ids = fields.One2many('sport.to.do.action', 'issue_id', string='To do actions')

    cost = fields.Float('Cost')

    user_phone = fields.Char('User Phone', related='user_id.phone', store=True,readonly=False)

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

    def _search_assigned(self,operator,value):
        if operator == '=':
            return [('user_id', operator, value)]
        else:
            return []
    
    def action_fill_tags(self):
        for record in self:
            import pdb;pdb.set_trace();
            similar_tags = self.env['sport.issue.tag'].search([('name','ilike',record.name)])
            if similar_tags:
                record.tag_ids = [(6,0,similar_tags.ids)]
                #record.tag_ids = [Command.set(similar_tags.ids)]
            else:
                #record.tag_ids = self.env['sport.issue.tag'].create({'name': record.name})
                record.tag_ids = [(0,0,{'name':record.name})]
                #record.tag_ids = [Command.create({'name':record.name})]

    def action_open(self):
        for record in self:
            record.state = 'open'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_done(self):
        for record in self:
            record.state = 'done'