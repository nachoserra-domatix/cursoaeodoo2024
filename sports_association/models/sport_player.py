from odoo import fields, models, api
from datetime import datetime

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'
    _inherits = {'res.partner': 'partner_id'}
  
    name = fields.Char(related='partner_id.name', inherited=True, readonly=False)
    birthday = fields.Date('Birthday', help='Birthday date', copy=False)
    years = fields.Integer(string='Years', help='Show age of player', compute='_compute_years', store=True)
    position = fields.Char(string='Position', copy=False)
    team_id = fields.Many2one('sport.team', string='Team', copy=False)
    tittle = fields.Boolean(string='Tittle',help='Show if the player is Principal', default=True, copy=False)
    sport_name = fields.Char('Sport', related='team_id.sport_id.name', store=True, copy=False)
    active = fields.Boolean('Active', default=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')
    
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
            
