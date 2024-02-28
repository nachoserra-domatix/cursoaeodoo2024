from odoo import fields, models

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sports Issues'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    date = fields.Date(string="Date")
    assistance = fields.Boolean(string="Assistance")
    state = fields.Selection(
        [('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done')
        ],
        string="State",
        default='draft'
    )

    user_id = fields.Many2one('res.users', string='User')
    secuence = fields.Integer(string='secuence', default=10)
    solution = fields.Html(string="Solution")
    
    clinic_id = fields.Many2one(
        string='Clinic',
        comodel_name='sport.clinic',
    )
    
    tag_ids = fields.Many2many(
        string='Tags',
        comodel_name='sport.issue.tag',
    )
    
    
    def action_open(self):
        for record in self:
            record.state = 'open'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_draft(self):
        for record in self:
            record.state = 'draft'            