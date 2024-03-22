# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class SportClinic(models.Model):
    _name = "sport.clinic"
    _description = "Sport Clinic"

    # === FIELDS ===#

    name = fields.Char(string="Name", required=True)
    phone = fields.Char("phone")
    email = fields.Char("email")
    issue_ids = fields.One2many(comodel_name="sport.issue", inverse_name="clinic_id")
    available = fields.Boolean("Available")
    issue_count = fields.Integer("Issue count", compute="_compute_issue_count")

    def _compute_issue_count(self):
        for record in self:
            record.issue_count = len(record.issue_ids)

    # === METHODS ===#

    def action_check_assistance(self):
        for record in self.issue_ids:
            record.assistance = True

    # === ACTIONS ===#

    def action_view_issues(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Issues",
            "view_mode": "tree,form",
            "res_model": "sport.issue",  # Cambia esto al modelo de incidencias correcto
            "domain": [("clinic_id", "=", self.id)],
        }
