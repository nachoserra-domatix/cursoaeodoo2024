from odoo import models, fields

class SportsTeam(models.Model):
    _name = 'sports.team'
    _description = 'Sports Team'

    name = fields.Char(string='Name',required=True)
    logo = fields.Image(string='Logo')
    players_ids = fields.One2many('sports.player','team_id',string='Players')
    sport_id = fields.Many2one('sports.sport',string='Sport')
    count_players = fields.Integer(string='Count Players',compute='_compute_count_players')
    
    def all_marked(self):
        for player in self.players_ids:
            player.make_starter()
        return True
    
    def all_substitute(self):
        for player in self.players_ids:
            player.make_substitute()
        return True
    
    def action_add_players(self):
        players = self.env['sports.player'].search([('team_id','=',False),('age','<',30)])
        for player in players:
            player.team_id=self.id
        return True
    
    def _compute_count_players(self):
        for record in self:
            record.count_players=len(record.players_ids)
