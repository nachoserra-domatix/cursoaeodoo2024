from odoo import models, fields, api
from datetime import date


class SportPlayer(models.Model):
    _name = "sport.player"
    _description = "Sport Player"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    position = fields.Char(string="Position")
    team_id = fields.Many2one('sport.team', string='Team')
    starter = fields.Boolean(string="Starter")
    photo = fields.Binary(string="Photo")
    sport_name = fields.Char('Sport Name', related='team_id.sport_id.name')
    birthdate = fields.Date('Date')

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate and record.birthdate <= date.today():
                self.age = (date.today() - self.birthdate).days // 365.25

    def check_starter(self):
        self.starter = True

    def uncheck_starter(self):
        self.starter = False
    
