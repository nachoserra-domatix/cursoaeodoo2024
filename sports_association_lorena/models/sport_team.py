from odoo import models, fields, Command

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char(string="Nombre", required=True)
    logo = fields.Binary(string="Logo")
    player_ids = fields.One2many('sport.player', 'team_id', string='Players')
    sport_id = fields.Many2one('sport.sport', string='Sport')

    def mark_headline(self):
        for player in self.player_ids:
            player.headline = True

    def desmark_headline(self):
        for player in self.player_ids:
            player.headline = False

    def action_add_players(self):
        for record in self:
            players = self.env['sport.player'].search([('team_id', '=', False), ('age', '<', 30)])
            record.player_ids = [Command.set(players.ids)]