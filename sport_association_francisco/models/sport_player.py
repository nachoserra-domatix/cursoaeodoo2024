from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class SportPlayer(models.Model):

    _name = 'sport.player'
    _description = 'Sport Player'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', string='Partner', ondelete="cascade", required=True)
    name = fields.Char(string="Name", related="partner_id.name",readonly=False, copy=False, inherited=True)
    age = fields.Integer(string='Age', compute='_computed_age', store=True, copy=False)
    position = fields.Char(string='Position', copy=False)
    team_id = fields.Many2one('sport.team', string='Team')
    titular = fields.Boolean(string='Titular', default=True, copy=False)
    sport_name = fields.Char('Sport Name', related='team_id.sport_id.name', store=True, copy=False)
    birth_date = fields.Date('Birth Date', copy=False)
    street = fields.Char(related="partner_id.street", inherited=True, readonly=False)

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
