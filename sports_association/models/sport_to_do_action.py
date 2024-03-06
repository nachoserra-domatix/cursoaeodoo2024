from odoo import models, fields

class SportToDoAction(models.Model):
    _name = 'sport.to.do.action'
    _description = "Sport Issue"
    
    name = fields.Char(string='Name', required=True)
    state = fields.Selection([
        ('draft','Draft'),
        ('open','Open'),
        ('done','Done')
        ],
        string='State',
        default='draft'
    )  

    issue_id = fields.Many2one('sport.issue', string='Issue')