from odoo import fields, models


class SportIssueAction(models.Model):
    _name = "sport.issue.action"
    _description = "Sports Issue Actions To Do"

    name = fields.Char(string="Name")
    state = fields.Selection(
        [("draft", "Draft"), ("open", "Open"), ("done", "Done")],
        string="State",
    )
    issue_id = fields.Many2one(
        string="Issue",
        comodel_name="sport.issue",
    )
