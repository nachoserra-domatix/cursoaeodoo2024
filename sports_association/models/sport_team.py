from odoo import models, fields, Command



class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char(string='Name', required=True, translate=True)
    logo = fields.Image(string='Logo')
    color = fields.Integer(string='Color')
    player_ids = fields.One2many(comodel_name='sport.player', inverse_name='team_id', string='Jugadores')
    sport_id = fields.Many2one(comodel_name='sport.sport', string='Sport')
    
    def set_starters(self):
        for player in self.player_ids:
            player.set_starter()
    
    def set_substitutes(self):
        for player in self.player_ids:
            player.set_substitute()

    def action_add_players(self):
        for record in self:
            players = self.env['sport.player'].search([('team_id', '=', False),('age','<',30)])
            record.player_ids = [Command.set(players.ids)]
            # for player in players:
            #     player.team_id = record.id
    
    
