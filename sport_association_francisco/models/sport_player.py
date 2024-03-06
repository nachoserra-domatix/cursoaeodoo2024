from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class SportPlayer(models.Model):

    _name = 'sport.player'
    _description = 'Sport Player'

    name = fields.Char(string="Name")
    age = fields.Integer(string='Age', compute='_computed_age', store=True)
    position = fields.Char(string='Position')
    team_id = fields.Many2one('sport.team', string='Team')
    titular = fields.Boolean(string='Titular')
    sport_name = fields.Char('Sport Name', related='team_id.sport_id.name')
    birth_date = fields.Date('Birth Date')

    @api.depends('birth_date')
    def _computed_age(self):
        for rec in self:
            if rec.birth_date:
                time_diference = relativedelta(datetime.now().date(), rec.birth_date)
                rec.age = time_diference.years
            else:
                rec.age = False

    def mark_as_titular(self):
        self.write({
            "titular": True
        })

    def unmark_as_titular(self):
        self.write({
            "titular": False
        })
