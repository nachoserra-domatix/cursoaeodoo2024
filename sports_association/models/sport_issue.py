from odoo import models, fields, api, _


class SportIssue(models.Model):
    _name = "sport.issue"
    _description = "Sport Issue"

    name = fields.Char(string=_("Name"), required=True)
    description = fields.Text(string="Description")
    date = fields.Date(string=_("Date"))
    assistance = fields.Boolean(
        string="Assistance", help="Show if the issue has assistance"
    )
    state = fields.Selection(
        [("draft", "Draft"), ("open", "Open"), ("done", "Done")],
        string="State",
        default="draft",
    )
    color = fields.Integer(string="Color", default="0")
    cost = fields.Float("Cost")
    user_id = fields.Many2one("res.users", string="User")
    sequence = fields.Integer(string="Sequence", default=10)
    solution = fields.Html("Solution")
    clinic_id = fields.Many2one("sport.clinic", string="Clinic")
    tag_ids = fields.Many2many("sport.issue.tag", string="Tags")
    assigned = fields.Boolean("Assigned", compute="_compute_assigned")

    def action_search_tag(self):
        for record in self:
            tag_ids = self.env["sport.issue.tag"].search(
                [("name", "ilike", record.name)]
            )
            if tag_ids:
                record.write(
                    {
                        "tag_ids": [(6, 0, tag_ids.ids)],
                    }
                )
            else:
                record.write(
                    {
                        "tag_ids": [(0, 0, {"name": record.name})],
                    }
                )

    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    def action_open(self):
        for record in self:
            record.state = "open"

    def action_draft(self):
        for record in self:
            record.state = "draft"

    def action_done(self):
        for record in self:
            record.state = "done"
