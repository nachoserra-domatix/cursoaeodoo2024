from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SportLeague(models.Model):
    _name = 'sport.league'
    _description = "Sport League"

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    league_line_ids = fields.One2many('sport.league.line', 'league_id', string='League Lines')
    game_ids = fields.One2many('sport.game', 'league_id', string='Games')
    game_count = fields.Integer('game_count', compute='_compute_game_count')

    @api.constrains('start_date','end_date')
    def _verify_end_date(self):
        for record in self:
            if record.start_date > record.end_date:
                raise ValidationError(_("The start date must be before than the end date"))

    def set_score(self):
        for record in self.league_line_ids:
            team = record.team_id
            score_points = self.env['sport.game'].search([('winner_team_id','=',team.id)]).mapped('winner_points')
            record.points = sum(score_points)

    def _cron_set_score(self):
        leagues = self.search([])
        leagues.set_score()

    def _compute_game_count(self):
        for record in self:
            record.game_count = len(record.game_ids)

    #Smart Button
    def action_view_games(self):
        return {
            'name': 'Games',
            'type' : 'ir.actions.act_window',
            'res_model' : 'sport.game',
            'view_mode': 'tree,form',
            'domain' : [('league_id', '=', self.id)]
        }
