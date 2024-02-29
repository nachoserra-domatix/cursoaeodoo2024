from odoo import _, api, fields, models

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char(string="Name", required=True)
    logo = fields.Binary(string="Team Logo")
    player_ids = fields.One2many("sport.player", "team_id", string="Players")
    sport_id = fields.Many2one("sport.sport")
    # trainer = fields.Many2one('res.partner')
    
    def add_all_titular(self):
        for player in self.player_ids:
            player.add_titular()
            
    def remove_all_titular(self):
        for player in self.player_ids:
            player.remove_titular()