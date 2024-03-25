from odoo import fields, models


class SportCreateIssue(models.TransientModel):
    _name = "sport.create.issue"
    _description = "Sport Create Issue"

    name = fields.Char("Issue Name")
    clinic_id = fields.Many2one(
        string="Clinic",
        comodel_name="sport.clinic",
    )
    player_id = fields.Many2one(
        string="Player",
        comodel_name="sport.player",
    )

    def create_issue(self):
        active_id = self.env.context.get("active_id")
        if self.env.context.get("active_model") == "sport.clinic":
            clinic_id = self.env["sport.clinic"].browse(active_id)
            self.clinic_id = clinic_id
        elif self.env.context.get("active_model") == "sport.player":
            player_id = self.env["sport.player"].browse(active_id)
            self.player_id = player_id
        vals = {
            "name": self.name,
            "clinic_id": self.clinic_id.id,
            "player_id": self.player_id.id,
        }
        issue = self.env["sport.issue"].create(vals)
        return {
            "name": "Issue",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "sport.issue",
            "res_id": issue.id,
            "target": "current",
        }
