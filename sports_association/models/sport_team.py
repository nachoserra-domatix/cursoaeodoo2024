from odoo import models, fields

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = "Sport Team"

    name = fields.Char(string='Name', required=True)
    logo = fields.Image(string='Logo', max_width='300px', max_height='300px')
    player_ids = fields.One2many('sport.player', 'team_id', string='Players')
    sport_id = fields.Many2one('sport.sport', string='Sport')

    def action_mark_players_regular(self):
        for record in self.player_ids:
            record.regular = True;

    def action_unmark_players_regular(self):
        for record in self.player_ids:
            record.regular = False;