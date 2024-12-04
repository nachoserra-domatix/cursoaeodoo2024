from odoo import models, fields



class SportLeagueLine(models.Model):
    _name = 'sport.league.line'
    _description = 'Sport League Line'
    
    league_id = fields.Many2one(comodel_name='sport.league', string='League')
    team_id = fields.Many2one(comodel_name='sport.team', string='Team')
    points = fields.Integer(string='Points')
    
    
    
    
    
    
    
