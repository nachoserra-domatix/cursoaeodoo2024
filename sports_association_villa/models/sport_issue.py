from odoo import fields, models

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

    def action_open(self):
        for record in self:
            record.state = 'open'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_done(self):
        for record in self:
            record.state = 'done'
