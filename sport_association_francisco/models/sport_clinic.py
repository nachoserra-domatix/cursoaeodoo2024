from odoo import models, fields, api

class SportClinic(models.Model):

    _name = 'sport.clinic'
    _description = 'Sport Clinic'

    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    available = fields.Boolean('Available')
    issue_ids = fields.One2many('sport.issue', 'clinic_id',string="Issues")
    issue_count = fields.Integer('Issues', compute="compute_total_issues", store=True)
    
    @api.depends('issue_ids')
    def compute_total_issues(self):
        for rec in self:
            rec.issue_count = len(rec.issue_ids)

    def action_check_assistance(self):
        self.issue_ids.write({
            'assistance': True
        })

    def action_view_issues(self):
        return{
            "name": "Issues",
            "type": 'ir.actions.act_window',
            "view_mode": 'tree,form',
            "res_model": "sport.issue",
            "domain": [('clinic_id', '=', self.id)],
        }
