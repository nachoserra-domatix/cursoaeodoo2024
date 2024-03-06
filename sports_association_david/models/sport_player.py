from odoo import _, api, fields, models
from datetime import datetime

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    birth_date = fields.Datetime(string="Birth Date")
    position = fields.Char()
    team_id = fields.Many2one("sport.team")
    titular = fields.Boolean(string="Titular")
    sport_name = fields.Many2one(related="team_id.sport_id")
    

    def add_titular(self):
        self.write({'titular' : True})

    def remove_titular(self):
        self.write({'titular' : False})

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            record.age = (datetime.today().date() - record.birth_date.date()).days // 365
        else:
            record.age = 0