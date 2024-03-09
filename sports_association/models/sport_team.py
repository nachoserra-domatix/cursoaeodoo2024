from odoo import fields, models

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Team Description'
  
    name = fields.Char(string='Name', required=True)
    player_list_ids = fields.One2many('sport.player', 'team_id', string='Player List')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    logo = fields.Image(string='Logo', max_width=100, max_height=100)
    color = fields.Integer('color', default=0)    

    # cambiamos el estado a todas
    def action_principal_all(self):
        self.player_list_ids.action_principal()        
        
    def action_secondary_all(self):
        self.player_list_ids.action_secondary()           
  