from odoo import fields, api, models

class SportCreateIssue(models.TransientModel):
    _name = "sport.create.issue"
    _description = "Create Issue"

    name = fields.Char(string="Issue name")
    clinic_id = fields.Many2one(comodel_name="sport.clinic")

    def create_issue(self):
        issue = self.env["sport.issue"].create(
            {
                "name": self.name,
                "clinic_id": self.clinic_id.id,
            }
        )
        return {
            "name": "Issue",
            "view_mode": "form",
            "res_model": "sport.issue",
            "res_id": issue.id,
            "type": "ir.actions.act_window",
            "target": "current",
        }

