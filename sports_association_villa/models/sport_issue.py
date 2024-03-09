from odoo import fields, models, api, Command


class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    date = fields.Date('Date')
    assistance = fields.Boolean(string='Assistance', help='Check if the issue has assistance')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done')], 
        string = 'State',
        default='draft')

    user_id = fields.Many2one('res.users', string='User') # User responsible for the issue, by default the creator of the issue
    sequense = fields.Integer(string = 'Sequense', default=10)
    solution = fields.Html('Solution')
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')
    tag_ids = fields.Many2many('sport.issue.tag', string='Tags')
    sport_action_to_do_ids = fields.One2many('sport.action.to.do', 'sport_issue_id', string='Actions to do')
    color = fields.Integer(string ='Color', default=0)
    cost = fields.Float('Cost')
    assigned = fields.Boolean('Assigned', compute='_compute_assigned', inverse='_inverse_assigned', search = '_search_assigned', store=True)
    user_phone = fields.Char('Phone', related='user_id.partner_id.phone', readonly=True)

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    def _inverse_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id = record.env.user

    def _search_assigned(self, operator, value):
        if operator == '=':
            return [('user_id', operator, bool(value))]
        else:
            return []

    def action_open(self):
        for record in self:
            record.state = 'open'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_add_tag(self):
        for record in self:
            # import wdb; wdb.set_trace()
            tag_ids = self.env['sport.issue.tag'].search([('name', 'ilike', 'record.name')])
            if tag_ids:
                # before_tag_ids = record.tag_ids
                # final_tag_ids |= before_tag_ids + tag_ids
                record.tag_ids = [Command.set(tag_ids.ids)]
                # record.tag_ids = [(6, 0 tag_ids.ids)]
            else:
                record.tag_ids = [Command.create({'name': record.name})]
                # record.tag_ids = [0, 0, ({'name': record.name})]

