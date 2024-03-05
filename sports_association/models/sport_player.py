from odoo import models, fields, api, _
from datetime import date


class SportPlayer(models.Model):
    _name = "sport.player"

    name = fields.Char(string=_("Name"), required=True)
    age = fields.Integer(string=_("Age"), compute="_compute_age", store=True)
    position_id = fields.Many2one(
        string=_("Position"), comodel_name="sport.player.position", required=True
    )
    team_id = fields.Many2one(
        string=_("Team"),
        comodel_name="sport.team",
    )
    sport_id = fields.Many2one(
        string=_("Sport"), comodel_name="sport.sport", related="team_id.sport_id"
    )

    headline = fields.Boolean(string=_("Headline"))
    sport_name = fields.Char(string=_("Sport"), related="team_id.sport_id.name")
    birth_date = fields.Date(string=_("Birth date"))

    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            record.age = (date.today() - record.birth_date).days // 365
