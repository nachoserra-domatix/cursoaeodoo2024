from odoo import api,models, fields
from dateutil.relativedelta import relativedelta

class Sportplayer(models.Model):
    _name = "sport.player"
    _description = "Sport Player"

    name = fields.Char(
        string='Name',
        copy=False
    )
    age = fields.Integer(
        string='Age',
        compute='_compute_age',
        store=True,
        copy=False
    )
    position = fields.Char(
        string='Position',
        copy=False
    )
    team_id = fields.Many2one(
        string='Team',
        comodel_name='sport.team',
    )
    starter = fields.Boolean(
        string='Starter',
        default=True,
        copy=False
    )
    sport = fields.Char(
        string="Sport",
        related='team_id.sport_id.name',
        store=True,
        copy=False
    )
    birthdate = fields.Date(string="Birthdate", copy=False)
    active = fields.Boolean(string="Active", default=True)


    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = relativedelta(fields.Date.today(), record.birthdate).years
            else:
                record.age = 0
        

    def action_check_starter(self):
        for record in self:
            record.starter = True

    def action_uncheck_starter(self):
        for record in self:
            record.starter = False
