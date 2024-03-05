# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, Command

class SportIssue(models.Model):
    _name ='sport.issue'
    _description = 'Description'
    
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    assistance = fields.Boolean(string='Assistance',help='Show if the issue has assistance')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done'),],
        string='State',
        default='draft',
    )
    
    color = fields.Integer('color', default=0)    
    user_id = fields.Many2one('res.users', string='User')
    sequence = fields.Integer('Sequence', default=10)
    solution = fields.Html('Solution')
    cost = fields.Float('Cost')
  
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')
    tag_ids = fields.Many2many('sport.issue.tag', string='Tags')
    
    assigned = fields.Boolean('Assigned', compute='_compute_assigned')
    
    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    # cambiamos el estado a las selecionadas a open
    # def action_open(self):
    #     self.write({'state':'open'})


    def action_open(self):
        for record in self:
            record.state = 'open'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_done(self):
        for record in self:
            record.state = 'done'
            
            
    def action_add_tags(self):
            for record in self:
                tag_ids = self.env['sport.issue.tag'].search([('name', 'ilike', record.name)])
                if tag_ids:
                    record.tag_ids = [Command.set(tag_ids.ids)]
                    #record.tag_ids = [(6, 0, tag_ids.ids)]
                else:
                    record.tag_ids = [Command.create({'name': record.name})]
                    #record.tag_ids = [(0, 0, {'name' : record.name})]

            
            
    # cambiamos el estado a todas
    # def action_open_all_issues(self):
    #     issues = self.env['sport.issue'].search([])
    #     issues.action.open()
        
        