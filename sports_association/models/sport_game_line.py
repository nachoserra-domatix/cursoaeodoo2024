from odoo import models, fields

class SportGameLine(models.Model):
    _name = 'sport.game.line'
    _description = "Sport Game Line"
    _order = "points desc"

    team_id = fields.Many2one('sport.team', string='Team')
    points = fields.Integer('Points')
    game_id = fields.Many2one('sport.game', string='Game')