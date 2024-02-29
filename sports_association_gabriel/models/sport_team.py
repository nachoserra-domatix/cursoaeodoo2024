from odoo import models, fields


class SportTeam(models.Model):
    _name = "sport.team"
    _description = "Sport Team"

    name = fields.Char(string='Name', required=True)
    player_ids = fields.One2many('sport.player', 'team_id', string='Players')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    logo = fields.Binary(string="Logo")

    def action_check_players_starter(self):
        for record in self.player_ids:
            record.check_starter()

    def action_uncheck_players_starter(self):
        for record in self.player_ids:
            record.uncheck_starter()
