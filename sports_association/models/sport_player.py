from odoo import models, fields, api
from datetime import date

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = "Sport Player"

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Birth Date')
    position = fields.Char(string='Position')
    team_id = fields.Many2one('sport.team',string='Team')
    regular = fields.Boolean(string='Regular')
    sport_name = fields.Char('Sport Name', related='team_id.sport_id.name')
    age = fields.Integer('Age', compute='_compute_age', store=True)

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            #if (isinstance(record.birth_date, date)):
            if record.birth_date:
                today = date.today()
                record.age = today.year - record.birth_date.year - ((today.month, today.day) < (record.birth_date.month, record.birth_date.day))
                # https://stackoverflow.com/questions/2217488/age-from-birthdate-in-python
                # today = fields.Date.today()
                # record.age = (today - record.birth_date).days / 365
            else:
                record.age = 0
            

    def action_mark_regular(self):
        for record in self:
            record.regular = True;

    def action_unmark_regular(self):
        for record in self:
            record.regular = False;