from odoo import models, fields

class SportGame(models.Model):
    _name = 'sport.game'
    _description = "Sport Game"

    name = fields.Char('Name')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    game_date = fields.Date('Game date')
    winner_team_id = fields.Many2one('sport.team', string='Winner Team')
    winner_points = fields.Integer('Winner points', default=3)
    league_id = fields.Many2one('sport.league', string='League')
    game_line_ids = fields.One2many('sport.game.line', 'game_id', string='Game Line')