from odoo import models, fields, Command

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char(string='Name', required=True)
    logo = fields.Image(string='Logo')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    player_ids = fields.One2many('sport.player', 'team_id', string="Players")
    player_count = fields.Integer(string='Player Count', compute='_compute_player_count')

    def _compute_player_count(self):
        for record in self:
            record.player_count = len(record.player_ids)
    
    def action_mark_starters(self):
        for player in self.player_ids:
            player.action_markself_starter()
    
    def action_unmark_starters(self):
        self.player_ids.write({'starter': False})

    def action_add_players(self):
        for record in self:
            # import pdb; pdb.set_trace()
            # import wdb; wdb.set_trace()
            players = self.env['sport.player'].search([('team_id', '=', False), ('age','<',30)])

            # for player in players:
            #     player.team_id = self.id

            players |= record.player_ids
            record.player_ids = [Command.set(players.ids)]

    def action_view_players(self):
        return {
            'name': 'Players',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.player',
            'view_mode': 'tree,form',
            'domain': [('team_id', '=', self.id)],
        }