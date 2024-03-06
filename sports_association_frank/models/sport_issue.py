from odoo import models, fields, api

class SportIssue(models.Model):
    _name = "sport.issue"
    _description = "Sport Issue"

    # Clase
    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    date = fields.Date(string="Date")
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
    user_phone = fields.Char(related="user_id.phone")
    action_ids = fields.One2many('sport.issue.action', 'issue_id', string='Actions to do')

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

    def action_open(self):
        self.write({"state": "open"})

    def action_draft(self):
        self.write({"state": "draft"})

    def action_done(self):
        for rec in self:

            rec.state = "done"

    def action_done_all_issues(self):
        issues = self.search([])
        issues.action_done()

    def action_add_tag(self):
        for rec in self:
            tag_ids = self.env['sport.issue.tag'].search([('name', 'ilike', rec.name)])
            rec.tag_ids = (tag_ids and [(6, 0, tag_ids.ids)]) or [(0, 0, {'name': rec.name})]

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
