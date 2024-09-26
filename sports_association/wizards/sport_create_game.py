from odoo import models, fields, api, Command, _


class SportCreateGame(models.TransientModel):
    _name = 'sport.create.game'
    _description = "Create game"

    name = fields.Char(string='Name', required=True)
    game_date = fields.Date('Game Date')
    league_id = fields.Many2one('sport.league', string='League', default= lambda self: self.env.context.get('active_id'))
    allowed_team_ids = fields.Many2many('sport.team', relation='sport_game_team_rel', string='allowed_team', compute='_compute_allowed_team_ids', store=True)
    team_ids = fields.Many2many('sport.team', string='Teams')
    

    @api.depends('league_id')
    def _compute_allowed_team_ids(self):
        for record in self:
            self.allowed_team_ids = self.league_id.league_line_ids.team_id.ids

    
    def create_game(self):

        vals = {
            'name': self.name,
            'game_date': self.game_date,
            'league_id': self.league_id.id,
            'game_line_ids': [(0,0, {'team_id': team.id}) for team in self.team_ids]
            }
        game = self.env['sport.game'].create(vals)
        
        return {
            'name': 'Game',
            'view_mode': 'form',
            'res_model' : 'sport.game',
            'res_id': game.id,
            'type': 'ir.actions.act_window',
            'target': 'current'
        }