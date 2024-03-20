from odoo import models, fields, api
from datetime import date


class SportPlayer(models.Model):
    _name = "sport.player"
    _description = "Sport Player"
    _inherits = {'res.partner': 'partner_id'}

    name = fields.Char(related='partner_id.name', inherited=True, readonly=False)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')
    age = fields.Integer(string="Age", compute='_compute_age', store=True, copy=False)
    position = fields.Char(string="Position", copy=False)
    team_id = fields.Many2one('sport.team', string='Team')
    starter = fields.Boolean(string="Starter", default="True", copy=False)
    photo = fields.Binary(string="Photo", copy=False)
    sport_name = fields.Char('Sport Name', related='team_id.sport_id.name', store=True)
    birthdate = fields.Date('Date', copy=False)
    active = fields.Boolean('Active', default=True)

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate and record.birthdate <= date.today():
                self.age = (date.today() - self.birthdate).days // 365.25
            else:
                self.age = 0

    def check_starter(self):
        self.starter = True

    def uncheck_starter(self):
        self.starter = False
    
