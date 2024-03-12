from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

class SportIssue(models.Model):
    _name = "sport.issue"
    _description = "Sport Issue"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    date = fields.Date(default=fields.Date.today)
    assistance = fields.Boolean(string="Assistance", help="Show if the issue has assistance")
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("open", "Open"),
            ("done", "Done"),
        ],
        string="State",
        default="draft",
    )
    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Responsible",
        default=lambda self: self.env.user,
    )
    sequence = fields.Integer(string="Sequence")
    solution = fields.Html(string="Solution")
    clinic_id = fields.Many2one(
        comodel_name="sport.clinic",
        string="Clinic",
    )
    tag_ids = fields.Many2many(
        comodel_name="sport.issue.tag",
        string="Tags",
    )
    color = fields.Integer(string="Color", default=0)
    cost = fields.Float(string="Cost")
    assigned = fields.Boolean(compute="_compute_assigned", inverse="_inverse_assigned", search="_search_assigned")
    user_phone = fields.Char()
    action_ids = fields.One2many('sport.issue.action', 'issue_id', string='Actions to do')

    @api.onchange("user_id")
    def _onchange_user_phone(self):
        for rec in self:
            rec.user_phone = rec.user_id.partner_id.phone

    def _compute_assigned(self):
        for rec in self:
            rec.assigned = bool(rec.user_id)

    def _inverse_assigned(self):
        for rec in self:
            if not rec.assigned:
                rec.user_id = False
            else:
                rec.user_id = self.env.user

    def _search_assigned(self, operator, value):
        return [("user_id", operator, value)]

    @api.constrains("cost")
    def _check_cost(self):
        for rec in self:
            if rec.cost < 0:
                raise ValidationError(_("Cost must be positive"))

    @api.onchange("clinic_id")
    def _onchange_clinic_id(self):
        for rec in self:
            if rec.clinic_id:
                rec.assistance = True
            else:
                rec.assistance = False

    def action_open(self):
        for rec in self:
            rec.state = "open"

    def action_draft(self):
        for rec in self:
            rec.state = "draft"

    def action_done(self):
        for rec in self:
            if not rec.date:
                raise UserError(_("Date is required"))
            rec.state = "done"

    def action_done_all_issues(self):
        issues = self.search([])
        issues.action_done()

    def action_add_tag(self):
        for rec in self:
            tag_ids = self.env['sport.issue.tag'].search([('name', 'ilike', rec.name)])
            rec.tag_ids = (tag_ids and [(6, 0, tag_ids.ids)]) or [(0, 0, {'name': rec.name})]

    def _cron_delete_unused_tags(self):
        issues = self.search([])
        tags = self.env['sport.issue.tag'].search([])
        unused_tags = issues.tag_ids - tags

    def action_sport_mark_done(self):
        ids = self.env.context.get("active_ids", False)
        if ids:
            issues = self.browse(ids)
            issues.state = "done"

    # Mis cambios
    # -----------------------------------------
    #
    priority = fields.Selection(
        selection=[
            ("1", "Low"),
            ("2", "Medium"),
            ("3", "High"),
        ],
    )        

    def name_get(self):
        result = []
        for rec in self:
            # primero nombre y despues si existe la fecha añadirla
            name = rec.name
            if rec.date:
                name = f"{name} - ({rec.date})"
            result.append((rec.id, name))
        return result
