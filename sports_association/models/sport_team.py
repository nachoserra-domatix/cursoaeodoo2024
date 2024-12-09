from odoo import Command, fields, models


class SportTeam(models.Model):
    _name = "sport.team"
    _description = "Sport Team"

    name = fields.Char(
        string="name",
    )

    player_ids = fields.One2many(
        string="Players",
        comodel_name="sport.player",
        inverse_name="team_id",
    )
    player_count = fields.Integer(
        string="Number of Players", compute="_compute_player_count"
    )
    sport_id = fields.Many2one(
        string="Sport",
        comodel_name="sport.sport",
    )

    game_line_ids = fields.One2many(
        string="Games",
        comodel_name="sport.game.line",
        inverse_name="team_id",
    )
    logo = fields.Image(
        string="Logo",
    )

    def _compute_player_count(self):
        for record in self:
            record.player_count = len(record.player_ids)

    def action_check_starter(self):
        for record in self:
            for player in record.player_ids:
                player.action_check_starter()

    def action_uncheck_starter(self):
        for record in self:
            for player in record.player_ids:
                player.action_uncheck_starter()

    def action_add_free_players(self):
        for record in self:
            free_players = self.env["sport.player"].search(
                [("team_id", "=", False), ("age", "<", 30)]
            )
            free_players |= record.player_ids
            record.player_ids = [Command.set(free_players.ids)]

    def action_view_players(self):
        return {
            "name": "Players",
            "type": "ir.actions.act_window",
            "res_model": "sport.player",
            "view_mode": "tree,form",
            "domain": [("team_id", "=", self.id)],
        }
