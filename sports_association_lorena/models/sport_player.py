from odoo import models, fields, api
from datetime import datetime

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', compute='_compute_age', store='True')
    position = fields.Char(string='Position')
    team_id = fields.Many2one('sport.team', string='Team')
    headline = fields.Boolean(string='Headline')
    sport = fields.Char(string='Sport', related='team_id.sport_id.name')
    date_birth = fields.Date(string='Date birth')

    @api.depends('date_birth')
    def _compute_age(self):
        hoy = datetime.now()
        for record in self:
            if record.date_birth:
                record.age = (hoy.date() - record.date_birth).days / 365
            else:
                record.age = 0