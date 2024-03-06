from odoo import models, fields, Command

class SportsIssue(models.Model):
    _name = 'sports.issue'
    _description = 'Sports Issue'

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    assistance = fields.Boolean(string='Assistance',help='Show if the issue has assitastance')
    state=fields.Selection(
        [('draft', 'Draft'),
          ('open', 'Open'),
          ('done','Done') ],
          string='State',
          default='draft')
    user_id = fields.Many2one('res.users', string='User')
    sequence = fields.Integer(string='Sequence',default=10)
    solution = fields.Html(string='Solution')
    clinic_id = fields.Many2one('sports.clinic', string='Clinic')
    tag_ids = fields.Many2many('sports.issue.tag', string='Tags')
    color = fields.Integer(string='Color Index',default=0)
    cost=fields.Float(string='Cost')
    assigned=fields.Boolean(string="Assigned",compute='_compute_asigned')

    def action_done(self):
        for record in self:
            record.state='done'
    
    def action_open(self):
        for record in self:
            record.state='open'
    
    def action_draft(self):
        for record in self:
            record.state='draft'
        
    def _compute_asigned(self):
        for issue in self:
            issue.assigned=bool(issue.user_id)

    
    def action_add_tag(self):
        for record in self:
            tag_ids = self.env['sports.issue.tag'].search([("name", "ilike", record.name)])
            if tag_ids:
                record.tag_ids = [Command.set(tag_ids.ids)]
                #record.tag_ids = [6,0,tag_ids.ids]
            else:
                record.tag_ids = [Command.create({'name': record.name})]
            
