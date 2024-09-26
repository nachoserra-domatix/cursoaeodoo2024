from odoo import models, fields, api, _
from datetime import datetime

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'
    _inherits = {"res.partner": "partner_id"}

    name = fields.Char(string='Name', inherited=True, readonly=False, related='partner_id.name',  translate=True, copy=False)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')
    date_of_birth = fields.Date(string='Date of birth', copy=False)
    age = fields.Integer(string='Age', compute='_compute_age', copy=False)
    position = fields.Char(string='Position', required=False, translate=True, copy=False)
    team_id = fields.Many2one(comodel_name='sport.team', string='Equipo')
    starter = fields.Boolean(string='Starter', default=True, copy=False)
    sport = fields.Char(string='Sport', related='team_id.sport_id.name', store=False, copy=False)
    
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

    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        if ('name' not in default) and ('partner_id' not in default):
            default['name'] = _("%s (copy)", self.name)
        return super().copy(default)