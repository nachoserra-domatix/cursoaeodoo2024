from odoo import _, api, fields, models

class SportToDo(models.Model):
    _name = 'sport.to.do'
    _description = 'Sport To Do'

    name = fields.Char(string="Name", required=True)
    state= fields.Selection(
        [('draft','Draft'),
         ('open','Open'),
         ('done','Done')], 
         string="State", 
         default='draft'
    )
    issue_id = fields.Many2one('sport.issue')