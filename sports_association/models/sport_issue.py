# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields

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
        
    user_id = fields.Many2one('res.users', string='User')
    sequence = fields.Integer('Sequence', default=10)
    solution = fields.Html('Solution')
    
    
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')

    tag_ids = fields.Many2many('sport.issue.tag', string='Tags')
    
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
            
    # cambiamos el estado a todas
    # def action_open_all_issues(self):
    #     issues = self.env['sport.issue'].search([])
    #     issues.action.open()
        
        