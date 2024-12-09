from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'
    _inherits = {'res.partner': 'partner_id'}

    #name = fields.Char(string='Name', required=True)
    name = fields.Char(related='partner_id.name', inherited=True, readonly=False)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')
    birthdate = fields.Date(string='Birthdate')
    age = fields.Integer(string='Age', compute='_compute_age', inverse='_inverse_age', search='_search_age', store=True)
    position = fields.Char(string='Position')
    starter = fields.Boolean(string='Starter', default=True)
    team_id = fields.Many2one('sport.team', string='Team')

    sport = fields.Char(string='Sport', related='team_id.sport_id.name', store=True)

    active = fields.Boolean(string='Active', default=True)

    def action_markself_starter(self):
        self.starter=True
    
    def action_unmarkself_starter(self):
        self.starter=False

    @api.depends('birthdate')
    def _compute_age(self):
        for player in self:
            if player.birthdate:
                player.age = (fields.Date.today() - player.birthdate).days // 365
    
    def _inverse_age(self):
        for player in self:
            if player.age:
                player.birthdate = fields.Date.today()-relativedelta(years=player.age)

    def _search_age(self, operator, value):
        if operator == '=':
            return [('birthdate', operator, fields.Date.today() - value * 365)]
        else:
            return []