from odoo import models, fields, api, Command
# import Pdb

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    assistance = fields.Boolean(string='Assistance', help='Show if the issue needs assistance')
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('open', 'Open'),
            ('done', 'Done'),
        ],
        string='State',
        default='draft',
    )

    color = fields.Integer(string='Color')
    user_id = fields.Many2one(comodel_name='res.users', string='User')
    sequence = fields.Integer(string='Sequence', default=10)
    solution = fields.Html(string='Solution')

    assigned = fields.Boolean(string='Assigned', compute='_compute_assigned', inverse='_inverse_assigned', search='_search_assigned')
    
    clinic_id = fields.Many2one(comodel_name='sport.clinic', string='Clinic')
    tag_ids = fields.Many2many(comodel_name='sport.issue.tag', string='')

    cost = fields.Float(string='Cost')

    user_phone = fields.Char(string='User phone', related='user_id.phone', store=True, readonly=False)
    
    @api.depends('user_id.phone')
    def _compute_assigned(self):
        for record in self:
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

    def action_draft(self):
        # pdb.set_trace()
        self.ensure_one()
        self.state = 'draft'
    
    def action_open(self):
        self.ensure_one()
        self.state = 'open'
    
    def action_done(self):
        self.ensure_one()
        self.env['sport.issue.tag'].create({})
        self.state = 'done'
    
    def action_add_tag(self):
        self.ensure_one()
        tag_ids = self.env['sport.issue.tag'].search([('name','ilike',self.name)])
        if tag_ids:
            self.tag_ids = [(6, 0, tag_ids.ids)]
        else:
            self.tag_ids = [Command.create({'name': self.name})]
