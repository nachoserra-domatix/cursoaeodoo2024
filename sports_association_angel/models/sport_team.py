from odoo import models, fields

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char(string='Name', required=True)
    logo = fields.Binary(string='Logo')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    player_ids = fields.One2many('sport.player', 'team_id', string="Players")

    def action_mark_starters(self):
        for player in self.player_ids:
            player.action_markself_starter()
    
    def action_unmark_starters(self):
        self.player_ids.write({'starter': False})