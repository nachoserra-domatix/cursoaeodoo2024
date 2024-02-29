from odoo import models, fields

class SportTeam(models.Model):
    _name = "sport.team"
    _description = "Sport Team"

    
    name = fields.Char(
        string='name',
    )
    
    
    player_ids = fields.One2many(
        string='Players',
        comodel_name='sport.player',
        inverse_name='team_id',
    )

    sport_id = fields.Many2one(
        string='Sport',
        comodel_name='sport.sport',
    )

        
    logo = fields.Image(
        string='Logo',
    )
    
    def action_check_starter(self):
        for record in self:
            for player in record.player_ids:
                player.starter = True

    def action_uncheck_starter(self):
        for record in self:
            for player in record.player_ids:
                player.starter = False