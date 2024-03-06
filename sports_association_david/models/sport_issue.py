from odoo import models, fields

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    date = fields.Datetime(string="Date")
    assistance = fields.Boolean(string="Assistance")
    state= fields.Selection(
        [('draft','Draft'),
         ('open','Open'),
         ('done','Done')], 
         string="State", 
         default='draft'
    )
    user_id = fields.Many2one('res.users', string="Usuario")
    sequence = fields.Integer(string="Sequence")
    solution = fields.Html(string="Solution")

    clinic_id = fields.Many2one('sport.clinic', string='Clinic')

    tag_ids = fields.Many2many('sport.issue.tag')

    color = fields.Integer(string='Color', default=0)
    cost = fields.Float(string='Cost')
    assigned = fields.Boolean(compute="_compute_assigned", string="Assigned")

    to_do_ids = fields.One2many('sport.to.do', 'issue_id', string="To Do")

    def action_open(self):
        for record in self:
            record.state = 'open'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def _compute_assigned(self):
        for record in self:
            if record.user_id:
                record.assigned = True
            else:
                record.assigned = False

    def action_add_tag(self):
        for record in self:
            tag_ids = self.env['sport.issue.tag'].search([('name','ilike', record.name)])
            if tag_ids:
                record.tag_ids = [(6,0, tag_ids.ids)]
            else:
                record.tag_ids = [(0,0, {'name': record.name })]


