from odoo import fields,api,models


class SportIssueMarkAlldone(models.TransientModel):
    _name = 'sport.issue.mark.all.done'
    _description = 'Sport Issue Mark All Done'

    
    def action_set_all_done(self):
        issues = self.env["sport.issue"].browse(self.env.context.get('active_ids'))
        issues.action_done()
        return {
            'name': 'Issue',
            'type': 'ir.actions.act_window',
            'view_mode': 'list',
            'res_model': 'sport.issue',
            'target': 'current'
        }
