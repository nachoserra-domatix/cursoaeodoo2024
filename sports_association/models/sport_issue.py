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
    color = fields.Integer(string="Color", default=0)
    cost = fields.Float(string="Cost")

    assigned = fields.Boolean(string="Assigned", compute="_compute_assigned", readonly=True)

    def _compute_assigned(self):
        self.assigned = False
        if self.user_id:
            self.assigned = True
    
    
    def action_open(self):
        for record in self:
            record.state = 'open'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_tags(self):
        for record in self:
            existing_tag_ids = self.env['sport.issue.tag'].search([('name', 'like', record.name)])
            if len(existing_tag_ids):
                record.tag_ids = [(6, 0, existing_tag_ids.ids)]
            else:
                self.env['sport.issue.tag'].create({'name': record.name})
