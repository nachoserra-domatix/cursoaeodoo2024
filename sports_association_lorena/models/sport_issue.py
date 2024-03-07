from odoo import models, fields, Command

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
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