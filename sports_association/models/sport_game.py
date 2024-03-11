from odoo import models, fields, api

class SportGame(models.Model):
    _name = "sport.game"
    _description = "Sport Game"

    
    league_id = fields.Many2one(string='League', comodel_name='sport.league')
    date = fields.Datetime(string='Date')
    team_winner_id = fields.Many2one(
        string='Winner',
        comodel_name='sport.team',
        compute="_compute_winner",
        store=True
    )
    team_looser_id = fields.Many2one(
        string='Looser',
        comodel_name='sport.team',
        compute="_compute_winner",
        store=True
    )
    points_winner = fields.Integer(string="Points Winner", related="league_id.points_winner")
    points_looser = fields.Integer(string="Points Looser", related="league_id.points_looser")
    game_line_ids = fields.One2many('sport.game.line', 'game_id', string='Game Scores')
    
    sport_id = fields.Many2one(
        string='Sport',
        comodel_name='sport.sport',
    )
    

    @api.depends('game_line_ids.score')
    def _compute_winner(self):
        for record in self:
            if record.game_line_ids:
                record.team_winner_id = max(record.game_line_ids, key=lambda x: x["score"]).team_id
                record.team_looser_id = min(record.game_line_ids, key=lambda x: x["score"]).team_id

