from odoo import models, fields

class SportGameLine(models.Model):
    _name = "sport.game.line"
    _description = "Sport Game Line"

    team_id = fields.Many2one(string='Team', comodel_name='sport.team')
    score = fields.Integer(string="Score")
    game_id = fields.Many2one(string='Game', comodel_name='sport.game')
    league_id = fields.Many2one(related='game_id.league_id')
