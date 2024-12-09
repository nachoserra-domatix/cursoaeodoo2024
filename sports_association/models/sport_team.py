from odoo import models, fields, Command

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = "Sport Team"

    name = fields.Char(string='Name', required=True)
    logo = fields.Image(string='Logo', max_width=300, max_height=300)
    player_ids = fields.One2many('sport.player', 'team_id', string='Players')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    players_count = fields.Integer('Players Count', compute='_compute_players_count')
    league_line_ids = fields.One2many('sport.league.line', 'team_id', string='League Lines')
    winner_game_ids = fields.One2many('sport.game', 'winner_team_id', string='Winner game')
    game_line_ids = fields.One2many('sport.game.line', 'team_id', string='Game Line')

    def _compute_players_count(self):
        for record in self:
            record.players_count = len(record.player_ids)

    def action_mark_players_regular(self):
        for record in self.player_ids:
            record.regular = True;

    def action_unmark_players_regular(self):
        for record in self.player_ids:
            record.regular = False;
    
    def action_add_young_players(self):
        for record in self:
            new_players = self.env['sport.player'].search([('age','<',30)])
            #record.player_ids = [(6,0,new_players.ids)]
            # new_players |= record.player_ids
            # record.player_ids = [Command.set(new_players.ids)]
            for player in new_players:
                player.team_id = self
        
    #Smart Button
    def action_view_players(self):
        return {
            'name': 'Players',
            'type' : 'ir.actions.act_window',
            'res_model' : 'sport.player',
            'view_mode': 'tree,form',
            'domain' : [('team_id', '=', self.id)]
        }