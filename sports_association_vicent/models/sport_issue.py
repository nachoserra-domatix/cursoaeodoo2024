# Copyright 2024 Vicent Esteve - vesteve@ontinet.com
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = "Sport Issue"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    assistance = fields.Boolean(string='Assistante', help='Show if the isuue has asssitence')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done')],
        string='State',
        default='draft',
    )
    user_id = fields.Many2one('res.users', string='User')
    sequence = fields.Integer(string='Sequence', default=10)
    solution = fields.Html('Solution')
    
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')
    tag_id = fields.Many2one('sport.issue.tag', string='Tags')
    

    def action_open(self):
        # import pdb:pdb.set_trace() --> para hacer como un debug o punto de interrupción
        # self.ensure_one() --> COmprobar que solo haya uno objecto en el self 
        # self.write({'state': 'open'}) -->Tambien sirve como bucle
        for record in self:
            record.state= 'open'
            
    def action_draft(self):
        for record in self:
            record.state= 'draft'
            
    def action_done(self):
        for record in self:
            record.state= 'done'         
        
    def action_open_all_issues(self):
        issues = self.env['sport.issue'].search([]) #Guardara todas las incidencias
        issues.action_open() #Llamrara al metodo de action_open
        