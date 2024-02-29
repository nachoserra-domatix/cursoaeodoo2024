from odoo import fields, models

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'
  
    name = fields.Char(string='Name', required=True)
    years = fields.Integer(string='Years')
    position = fields.Char(string='Position')
    team_id = fields.Many2one('sport.team', string='team')
    tittle = fields.Boolean(string='Tittle',help='Show if the player is Principal')
    

    def action_principal(self):
        for record in self:
            record.tittle = True

    def action_secondary(self):
        for record in self:
            record.tittle = False
            
