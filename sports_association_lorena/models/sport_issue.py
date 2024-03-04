from odoo import models, fields

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

    def action_open(self):
        for record in self:
            record.state = 'open'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_close(self):
        for record in self:
            record.state = 'close'