from odoo import models, fields

class SportIssue(models.Model):
    _name =  'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date',required=True)
    assistance = fields.Boolean(string='Assistance',help='Show if the issue had external assistance (paramedics)')
    state = fields.Selection(
        [('draft','Draft'),
         ('open','Open'),
         ('done','Done')],
         string='State',
         default='draft',
    )

    user_id = fields.Many2one('res.users', string='User')
    sequence = fields.Integer(string='Sequence', default=10)
    solution = fields.Html(string='Solution')

    clinic_id = fields.Many2one('sport.clinic', string='Clinic')   

    tags_ids = fields.Many2many('sport.issue.tag', string='Tags')
    color = fields.Integer(string="Color",default=0)
    cost =fields.Float(string="Cost", default=0.0)
                                 
    def action_open(self):
        # import pdb;pdb.set_trace()

        # self.ensure_one()
        for record in self:
            record.state = 'open'
        # self.write({'state': 'open'})
    
    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_done(self):
        for record in self:
            record.state = 'done'
            
    def action_open_all_issues(self):
        issues = self.env['sport.issue'].search([])
        issues.action_open()