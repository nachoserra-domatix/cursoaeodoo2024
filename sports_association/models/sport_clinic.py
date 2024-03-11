from odoo import models, fields, api

class SportClinic(models.Model):
    _name = "sport.clinic"
    _description = "Sport Clinic"

    name = fields.Char(
        string='name',
        required=True
    )
    phone = fields.Char(
        string='phone',
    )
    email = fields.Char(
        string='email',
    )
    issue_ids = fields.One2many(
        string='Issues',
        comodel_name='sport.issue',
        inverse_name='clinic_id',
    )
    available = fields.Boolean(
        string='Available',
    )

    issue_count = fields.Integer("Issue Count", compute="_compute_issue_count")
   
    @api.depends('issue_ids')
    def _compute_issue_count(self):
        for record in self:
            record.issue_count = len(record.issue_ids)
    
    
    def action_check_assistance(self):
        for record in self:
            for issue in record.issue_ids:
                issue.assistance = True

    def action_view_issues(self):
        return{
            "name": "Issues",
            "type": "ir.actions.act_window",
            "res_model": "sport.issue",
            "view_mode": "tree,form",
            "domain": [("clinic_id", '=', self.id)]
        }
