from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class Sportplayer(models.Model):
    _name = "sport.player"
    _description = "Sport Player"
    _inherits = {"res.partner": "partner_id"}

    name = fields.Char(
        string="Name", inherited=True, readonly=False, related="partner_id.name"
    )
    partner_id = fields.Many2one(
        "res.partner", string="Partner", required=True, ondelete="cascade"
    )
    age = fields.Integer(string="Age", compute="_compute_age", store=True, copy=False)
    position = fields.Char(string="Position", copy=False)
    team_id = fields.Many2one(
        string="Team",
        comodel_name="sport.team",
    )
    starter = fields.Boolean(string="Starter", default=True, copy=False)
    sport = fields.Char(
        string="Sport", related="team_id.sport_id.name", store=True, copy=False
    )
    birthdate = fields.Date(string="Birthdate", copy=False)
    active = fields.Boolean(string="Active", default=True)

    @api.depends("birthdate")
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

    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        if ("name" not in default) and ("partner_id" not in default):
            default["name"] = self.name
        return super().copy(default)
