from odoo import models, fields



class SportMatchLine(models.Model):
    _name = 'sport.match.line'
    _description = 'Sport match Line'
    
    match_id = fields.Many2one(comodel_name='sport.match', string='Match')
    team_id = fields.Many2one(comodel_name='sport.team', string='Team')
    points = fields.Integer(string='Points')
    
    
    
    
    
