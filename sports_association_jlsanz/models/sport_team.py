from odoo import models, fields

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char(string='Name', required=True)
    player_ids = fields.One2many('sport.player','team_id',string='Player')
    sport_id = fields.Many2one('sport.sport',string='Sport')
    logo = fields.Image(string='Logo')

    player_count = fields.Integer(string='Player_Count', compute='_calc_players') 

    def action_checkall_starter(self):
        for record in self.player_ids:
            #record.starter = True
            record.action_check_starter()

    def action_uncheckall_starter(self):
        for record in self.player_ids:
            #record.starter = False
            record.action_uncheck_starter()

    def _calc_players(self):
        for record in self:
            result_players = self.env['sport.player'].search([('team_id','=',record.id)])
            if result_players:
                record.player_count = len(result_players)
            else:
               record.player_count = 0
            #record.player_count = len(record.player_ids)

    def action_add_lonely_player(self):
        for record in self:
            result_players = self.env['sport.player'].search([('team_id','=',False), ('age', '<', 30)])
            if result_players:
                record.player_ids = [(6,0,result_players.ids)]

    # Smart button
    def action_view_players(self):
        return {
            'name': 'Players',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.player',
            'view_mode': 'tree,form',
            'domain': [('team_id', '=', self.id)],
        }