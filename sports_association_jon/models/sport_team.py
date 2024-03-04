from odoo import models, fields

class SportTeam(models.Model):
    _name = "sport.team"
    _description = "Sport Team"

    
    name = fields.Char(
        string='name',
    )
    
    player_ids = fields.One2many(
        'sport.player',
        'team_id',
        string='player',
    )
    
    
    sport_id = fields.Many2one(
        'sport.sport',
        string='sport',
    )
    
    logo = fields.Image("Logo")

    def change_player_status(self):
        for player in self.player_ids:
            if player.starter:
                player.starter_false()
            else:
                player.starter_true()