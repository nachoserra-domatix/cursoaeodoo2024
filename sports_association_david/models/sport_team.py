from odoo import _, api, fields, models

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char(string="Name", required=True)
    logo = fields.Binary(string="Team Logo")
    player_ids = fields.One2many("sport.player", "team_id", string="Players")
    sport_id = fields.Many2one("sport.sport")
    # trainer = fields.Many2one('res.partner')
    player_count = fields.Integer(string='Player_Count', compute='_compute_player_count')
    
    def add_all_titular(self):
        for player in self.player_ids:
            player.add_titular()
            
    def remove_all_titular(self):
        for player in self.player_ids:
            player.remove_titular()

    
    def action_add_players(self):
        for record in self:
            players = self.env['sport.player'].search([('team_id','=', False),('age','<', 30)])
            if players:
                record.player_ids = [(6,0,players.ids)]

    def _compute_player_count(self):
        for record in self:
            result_players = self.env['sport.player'].search([('team_id','=',record.id)])
            record.player_count = len(result_players)