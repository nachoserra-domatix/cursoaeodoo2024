# Copyright NuoBiT Solutions - Kilian Niubo <kniubo@nuobit.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models


class SportPlayer(models.Model):
    _name = "sport.player"
    _description = "Sport Player"
    name = fields.Char(
        required=True,
    )
    birthday = fields.Date(
        string="Date of Birth",
    )
    age = fields.Integer(
        compute="_compute_sport_player_age",
    )

    @api.depends("birthday")
    def _compute_sport_player_age(self):
        for rec in self:
            age = 0
            if rec.birthday:
                age = relativedelta(fields.Date.today(), rec.birthday).years
            rec.age = age

    position = fields.Char()
    # TODO: This field probably should be a m2m
    team_id = fields.Many2one(comodel_name="sport.team")
    titular = fields.Boolean()

    def set_true_titular_players(self):
        for rec in self:
            # comprobación menos costosa que asignación
            if not rec.titular:
                rec.titular = True

    def set_false_titular_players(self):
        for rec in self:
            # comprobación menos costosa que asignación
            if rec.titular:
                rec.titular = False

    def change_titularity(self):
        for rec in self:
            rec.titular = False if rec.titular else True
