from odoo import models, fields
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

    user_id = fields.Many2one(comodel_name='res.users', string='User')
    sequence = fields.Integer(string='Sequence', default=10)
    solution = fields.Html(string='Solution')
    
    clinic_id = fields.Many2one(comodel_name='sport.clinic', string='Clinic')
    tag_ids = fields.Many2many(comodel_name='sport.issue.tag', string='')
    
    
    def action_draft(self):
        # pdb.set_trace()
        self.ensure_one()
        self.state = 'draft'
    
    def action_open(self):
        self.ensure_one()
        self.state = 'open'
    
    def action_done(self):
        self.ensure_one()
        self.state = 'done'
    
