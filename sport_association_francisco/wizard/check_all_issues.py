from odoo import fields, api, models

class CheckAllIssues(models.TransientModel):
    _name = 'check.all.issues'
    _description = "Check all issues"

    date = fields.Date('Date')


    def check_all_issues(self):
        self.ensure_one()
        active_ids = self.env.context.get('active_ids')
        issues = self.env['sport.issue'].browse(active_ids)
        issues.action_done()
        if self.date:
            issues.write({
                'date':self.date
            })
        return {
            'type': 'ir.actions.act_window_close',
        }
