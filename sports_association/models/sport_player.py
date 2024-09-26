from odoo import models, fields, api, _
from datetime import date

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = "Sport Player"
    _inherits = {'res.partner': 'partner_id'}

    # name = fields.Char(string='Name', required=True)
    name = fields.Char(string='Name', related="partner_id.name", inherited=True, readonly=False ,required=True)
    partner_id = fields.Many2one('res.partner', string='partner', required=True, ondelete="cascade")
    birth_date = fields.Date(string='Birth Date', copy=False)
    position = fields.Char(string='Position', copy=False)
    team_id = fields.Many2one('sport.team',string='Team')
    regular = fields.Boolean(string='Regular', default=True, copy=False)
    sport_name = fields.Char('Sport Name', related='team_id.sport_id.name', store=True, copy=False)
    age = fields.Integer('Age', compute='_compute_age', store=True, copy=False)
    issue_ids = fields.One2many('sport.issue', 'player_id', string='Issues', copy=False)
    active = fields.Boolean('Active', default=True)

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
            record.regular = True

    def action_unmark_regular(self):
        for record in self:
            record.regular = False

    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        if ('name' not in default) and ('partner_id' not in default):
            default['name'] = _("%s (copy)", self.name)
        return super().copy(default)