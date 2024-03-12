from odoo import models, fields, api 

class SportsMarkIssueDone(models.TransientModel):
    _name = 'sports.mark.issue.done'
    _description = 'Mark Issue as Done'

    def mark_done(self):
        active_ids = self.env.context.get('active_ids')
        issues = self.env['sports.issue'].browse(active_ids)
        issues.write({'state': 'done'})