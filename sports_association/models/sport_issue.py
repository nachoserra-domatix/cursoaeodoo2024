# Copyright NuoBiT Solutions - Kilian Niubo <kniubo@nuobit.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)
from odoo import fields, models


class SportIssue(models.Model):
    _name = "sport.issue"
    _description = "Sport Issue"

    name = fields.Char(
        required=True,
    )
    description = fields.Text()
    date = fields.Date()
    assistance = fields.Boolean(
        help="Show if the issue has asssitence",
    )
    state = fields.Selection(
        [("draft", "Draft"), ("open", "Open"), ("done", "Done")],
        default="draft",
    )
    user_id = fields.Many2one(
        comodel_name="res.users",
    )
    sequence = fields.Integer(
        default=0,
    )
    solution = fields.Html("Solution")

    clinic_id = fields.Many2one(
        comodel_name="sport.clinic",
    )
    tag_id = fields.Many2one(
        comodel_name="sport.issue.tag",
    )

    def action_open(self):
        for rec in self:
            rec.state = "open"

    def action_draft(self):
        for rec in self:
            rec.state = "draft"

    def action_done(self):
        for record in self:
            record.state = "done"

    def action_open_all_issues(self):
        issues = self.env["sport.issue"].search([])
        issues.action_open()
