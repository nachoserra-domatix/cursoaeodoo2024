from odoo import models, fields

class SportsLeagueLine(models.Model):
    _name = 'sports.league.line'
    _description = 'Sports League Line'
    _order = 'points desc'
    _rec_name = 'team_id'
    league_id = fields.Many2one('sports.league',string='League')
    team_id = fields.Many2one('sports.team',string='Team')
    points = fields.Integer(string='Points')