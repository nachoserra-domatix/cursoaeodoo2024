from odoo import models, fields

class SportClinic(models.Model):
    _name = "sport.clinic"
    _description = "Sport Clinic"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    issue_ids = fields.One2many(
        comodel_name="sport.issue",
        inverse_name="clinic_id",
        string="Issues",
    )
    issue_count = fields.Integer(compute="_compute_issue_count")

    def _compute_issue_count(self):
        for rec in self:
            rec.issue_count = len(rec.issue_ids)

    def action_check_assistance():
        for rec in self:
            rec.issue_ids.write({"state": "done"})

    # smartbutton for issues
    def action_view_issues(self):
        self.ensure_one()
                
        return {
            "name": "Issues",
            "type": "ir.actions.act_window",
            "res_model": "sport.issue",
            "view_mode": "tree,form",
            "domain": [("clinic_id", "=", self.id)],
        }

    _sql_constraints = [
        ("name_uniq", "unique(name)", "Name must be unique"),
    ]
