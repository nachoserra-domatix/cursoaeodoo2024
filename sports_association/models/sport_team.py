from odoo import fields, models, Command

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team Description'
  
    name = fields.Char(string='Name', required=True)
    player_list_ids = fields.One2many('sport.player', 'team_id', string='Player List')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    logo = fields.Image(string='Logo', max_width=100, max_height=100)
    color = fields.Integer('color', default=0)    
    player_count = fields.Integer('Player Count', compute='_compute_player_count')

    def _compute_player_count(self):
        for record in self:
            record.player_count = len(record.player_list_ids)

    def action_add_players(self):
        for record in self:
            players = self.env['sport.player'].search([('team_id', '=', False), ('years', '<', 30)])
            players |= record.player_list_ids
            record.player_list_ids = [Command.set(players.ids)]

    # cambiamos el estado a todas
    def action_principal_all(self):
        self.player_list_ids.action_principal()        
        
    def action_secondary_all(self):
        self.player_list_ids.action_secondary()           
  
    def action_view_players(self):
        return {
            'name': 'Players',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.player',
            'view_mode': 'tree,form',
            'domain': [('team_id', '=', self.id)],
        }
            