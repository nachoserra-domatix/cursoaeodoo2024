from odoo import models, fields, api

class SportCreateMatch(models.TransientModel):
    _name = 'sport.create.match'
    _description = 'Create match'

    name = fields.Char('Match name')
    match_datetime = fields.Datetime('Date and time')
    team1_id = fields.Many2one('sport.team', string='Team 1')
    team2_id = fields.Many2one('sport.team', string='Team 2')
    league_id = fields.Many2one('sport.league', string='League', default=lambda self: self.env.context.get('active_id'))
    sport_id = fields.Many2one('sport.sport', string='Sport', related='league_id.sport_id')

    # team_ids = fields.Many2many('sport.team', string='Teams')

    def create_match(self):

        match_vals = {
            'name': self.name,
            'match_datetime': self.match_datetime,
            'league_id': self.league_id.id,
            'sport_id': self.sport_id.id,
            'match_line_ids': [(0, 0, {'team_id': self.team1_id.id}), (0, 0, {'team_id': self.team2_id.id})],
            # 'match_line_ids': [(0, 0, {'team_id': self.team.id}) for team in self.team_ids],
        }
        match = self.env['sport.match'].create(match_vals)
        
        # line1_vals = {
        #     'match_id': match.id,
        #     'team_id': self.team1_id.id,
        # }
        # line1 = self.env['sport.match.line'].create(line1_vals)
        # line2_vals = {
        #     'match_id': match.id,
        #     'team_id': self.team2_id.id,
        # }
        # line2 = self.env['sport.match.line'].create(line1_vals)
        

        return {
            'type': 'ir.actions.act_window', 
            'name': 'Match', 
            'res_model': 'sport.match', 
            'res_id': match.id, 
            'view_mode': 'form', 
            'target': 'current', }
        