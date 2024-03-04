from odoo import models, fields

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char(string='Name')
    description = fields.Text(string='Desciption')
    date = fields.Date(string='Date')
    assistance = fields.Boolean(string='Assistance', help="Show")
    state = fields.Selection(
        [('draft', 'Draft'),
         ('open', 'Open'),
         ('done', 'Done')],
        string='State',
        default='draft'
    )

    user_id = fields.Many2one('res.users', string="User")
    sequence = fields.Integer(string="Sequence", default="10")
    solution = fields.Html(string="Solutions")
    color = fields.Integer(string="Color", default=0)
    cost = fields.Float(string="cost")

    clinic_ids= fields.Many2one('sport.clinic', string='Clinic')

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

#    def action.open_all_issues(self):
#        for record in self:
#            action.open(record)
