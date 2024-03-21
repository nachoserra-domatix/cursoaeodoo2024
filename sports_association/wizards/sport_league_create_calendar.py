from odoo import fields, models, Command
from datetime import timedelta


class SportLeagueCreateCalendar(models.TransientModel):
    _name = "sport.league.create.calendar"
    _description = "Sport League Create Calendar"

    date_start = fields.Date(
        string="Start Date",
        default=fields.Date.context_today,
    )

    def create_calendar(self):
        active_id = self.env.context.get("active_id")
        league_id = self.env["sport.league"].browse(active_id)
        date_game = self.date_start

        # ToDo: better control dates for every week
        for i in range(len(league_id.league_line_ids)):
            date_game = self.date_start
            for j in range(i + 1, len(league_id.league_line_ids)):
                vals = {
                    "league_id": league_id.id,
                    "date": date_game,
                    "game_line_ids": [
                        Command.create(
                            {"team_id": league_id.league_line_ids[i].team_id.id}
                        ),
                        Command.create(
                            {"team_id": league_id.league_line_ids[j].team_id.id}
                        ),
                    ],
                }
                # import pdb; pdb.set_trace()
                self.env["sport.game"].create(vals)
                date_game += timedelta(weeks=1)

        return {
            "name": "League",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "sport.league",
            "res_id": league_id.id,
            "target": "current",
        }
