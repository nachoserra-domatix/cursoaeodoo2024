from odoo import _, api, fields, models

class SportCreateLeagueMatch(models.TransientModel):
    _name = 'sport.create.league.match'
    _description = 'Sport Create League match'

    league_id = fields.Many2one(comodel_name='sport.league', string='League')
    sport_id = fields.Many2one(comodel_name='sport.sport', string='Sport')
    team_ids = fields.Many2many(comodel_name='sport.team', string='Teams')
    date_and_time = fields.Datetime(string='Date')
    
    def create_league_match(self):
        vals = {
            'league_id': self.league_id.id,
            'sport_id': self.sport_id.id,
            'date_and_time': self.date_and_time,
            'match_line_ids': [(0, 0, {'team_id': team.id}) for team in self.team_ids],
            # 'winner_team_id': self.winner_team_id,
            # 'score_winning': self.score_winning,
        }
        league_match = self.env['sport.match'].create(vals)
        return {
            'name': 'Match',
            'view_mode': 'form',
            'res_model': 'sport.match',
            'res_id': league_match.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }