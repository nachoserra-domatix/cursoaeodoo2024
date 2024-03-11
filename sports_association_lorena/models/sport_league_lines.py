from odoo import models, fields

class SportLeagueLine(models.Model):
    _name = 'sport.league.line'
    _description = 'Sport League Line'

    team_id = fields.Many2one('sport.team', string='Team')
    rating = fields.Integer(string='Rating')
    league_id = fields.Many2one('sport.league', string='League')