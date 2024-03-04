from odoo import models, fields

class SportIssue(models.Model):

    _name = 'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    state = fields.Selection(string='State', selection=[('draft','Draft'),('open','Open'),('done','Done')], default='draft')
    assistance = fields.Boolean(string='Assistance')
    user_id = fields.Many2one(string='Usuario', comodel_name='res.users')
    sequence = fields.Integer(string='Sequence')
    solution = fields.Html(string='Solution')
    tag_ids = fields.Many2many('sport.tag', string='Tag')
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')
    color = fields.Integer(string='Color', default=0)
    cost = fields.Float('Cost')

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
