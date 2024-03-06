from odoo import models, fields, api
from datetime import datetime

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'

    name = fields.Char(string='Name', required=True, translate=True)
    date_of_birth = fields.Date(string='Date of birth')
    age = fields.Integer(string='Age', compute='_compute_age')
    position = fields.Char(string='Positionn', required=True, translate=True)
    team_id = fields.Many2one(comodel_name='sport.team', string='Equipo')
    starter = fields.Boolean(string='Starter')
    sport = fields.Char(string='Sport', related='team_id.sport_id.name', store=False)
    
    @api.onchange('date_of_birth')
    def _compute_age(self):
        for record in self:
            today = datetime.today()
            if record.date_of_birth:
                dob = datetime.strptime(str(record.date_of_birth), '%Y-%m-%d').date()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                record.age = age
            else:
                record.age = 0

    def set_starter(self):
        self.starter = True
    
    def set_substitute(self):
        self.starter = False