from odoo import models, fields, api

class SportGame(models.Model):
    _name = 'sport.game'
    _description = "Sport Game"

    name = fields.Char('Name')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    game_date = fields.Date('Game date')
    winner_team_id = fields.Many2one('sport.team', string='Winner Team', compute='_compute_winner_team', store=True)
    winner_points = fields.Integer('Winner points', default=3)
    league_id = fields.Many2one('sport.league', string='League')
    game_line_ids = fields.One2many('sport.game.line', 'game_id', string='Game Line')

    @api.depends('game_line_ids.points')
    def _compute_winner_team(self):
        for record in self:
            order_game_lines = record.game_line_ids.sorted(key=lambda r: r.points, reverse=True)
            if order_game_lines:
                record.winner_team_id = order_game_lines[0].team_id