from odoo import Command, api, fields, models
from odoo.exceptions import UserError, ValidationError


class SportIssue(models.Model):
    _name = "sport.issue"
    _description = "Sports Issues"
    _inherit = ["portal.mixin", "mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    date = fields.Date(string="Date", default=fields.Date.today)
    assistance = fields.Boolean(string="Assistance")
    state = fields.Selection(
        [("draft", "Draft"), ("open", "Open"), ("done", "Done")],
        string="State",
        default="draft",
        tracking=True,
    )
    user_id = fields.Many2one(
        "res.users", string="User", default=lambda self: self.env.user, tracking=True
    )
    player_id = fields.Many2one(string="Player", comodel_name="sport.player")
    phone_user = fields.Char("User Phone", readonly=True)
    secuence = fields.Integer(string="secuence", default=10)
    solution = fields.Html(string="Solution")
    clinic_id = fields.Many2one(
        string="Clinic",
        comodel_name="sport.clinic",
    )
    tag_ids = fields.Many2many(
        string="Tags",
        comodel_name="sport.issue.tag",
    )
    color = fields.Integer(string="Color", default=0)
    cost = fields.Float(string="Cost")
    assigned = fields.Boolean(
        string="Assigned",
        compute="_compute_assigned",
        inverse="_inverse_assigned",
        store=True,
    )
    actions_ids = fields.One2many(
        string="Actions To Do",
        comodel_name="sport.issue.action",
        inverse_name="issue_id",
    )

    _sql_constraints = [
        ("name_unique", "unique (name)", "The issue name must be unique!"),
    ]

    @api.constrains("cost")
    def _check_cost(self):
        for record in self:
            if record.cost < 0:
                raise ValidationError("The cost must be positive")

    @api.onchange("clinic_id")
    def _onchange_clinic_id(self):
        for record in self:
            if record.clinic_id:
                record.assistance = True
            else:
                record.assistance = False

    @api.onchange("user_id")
    def _onchange_user_id(self):
        for record in self:
            if record.user_id:
                record.phone_user = record.user_id.phone
            else:
                record.phone_user = False

    @api.depends("user_id")
    def _compute_assigned(self):
        for record in self:
            self.assigned = bool(record.user_id)

    @api.depends("user_id")
    def _inverse_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id = self.env.user

    def action_open(self):
        for record in self:
            record.state = "open"

    def action_done(self):
        for record in self:
            if record.date:
                record.state = "done"
            else:
                raise UserError("An issue date must be selected")
            msg_body = (
                f"This issue has been marked as {record.state} at date {record.date}"
            )
            record.message_post(body=msg_body)

    def action_draft(self):
        for record in self:
            record.state = "draft"

    def action_tags(self):
        for record in self:
            existing_tag_ids = self.env["sport.issue.tag"].search(
                [("name", "like", record.name)]
            )
            if len(existing_tag_ids):
                record.tag_ids = [Command.set(existing_tag_ids.ids)]
            else:
                record.tag_ids = [Command.create({"name": record.name})]
