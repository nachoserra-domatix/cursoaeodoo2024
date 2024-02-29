from odoo import models, fields

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