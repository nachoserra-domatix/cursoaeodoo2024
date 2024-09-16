from odoo import fields, models, api, Command

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char('Name', required=True)
    # logo = fields.Binary("Logo")
    logo = fields.Image("Logo", max_width=80, max_height=80)
    players_ids = fields.One2many('sport.player', 'team_id', string='Players')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    total_players = fields.Integer('Total Players', compute='_compute_total_players', store=True)
    color = fields.Integer(string ='Color', default=0)

    @api.depends('players_ids')
    def _compute_total_players(self):
        for record in self:
            record.total_players = len(record.players_ids)

    def action_check_starting_player_on(self):
        self.players_ids.write({'starting_player': True})

    def action_check_starting_player_off(self):
        self.players_ids.write({'starting_player': False})

    def action_add_players(self):
            players = self.env['sport.player'].search([('team_id', '=', False), ('age', '<', 30)])
            for player in players:
                player.team_id = self.id 
            return True

    def action_add_players(self):
        for record in self:
            players = self.env['sport.player'].search([('team_id', '=', False), ('age', '<', 30)])
            players |= record.players_ids
            record.players_ids = [Command.set(players.ids)]