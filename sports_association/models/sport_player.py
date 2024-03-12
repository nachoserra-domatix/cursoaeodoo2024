from odoo import fields, models, api
from datetime import datetime

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'
  
    name = fields.Char(string='Name', required=True)
    birthday = fields.Date('birthday')
    years = fields.Integer(string='Years', compute='_compute_years', store=True)
    position = fields.Char(string='Position')
    team_id = fields.Many2one('sport.team', string='team')
    tittle = fields.Boolean(string='Tittle',help='Show if the player is Principal')
    sport_name = fields.Char('Sport', related='team_id.sport_id.name', store=True)
    
    @api.depends('birthday')
    def _compute_years(self):
        for record in self:
            if record.birthday:
                record.years = (fields.Date.today() - record.birthday).days / 365
            else:
                record.years = 0
    
    def action_principal(self):
        for record in self:
            record.tittle = True

    def action_secondary(self):
        for record in self:
            record.tittle = False
            
