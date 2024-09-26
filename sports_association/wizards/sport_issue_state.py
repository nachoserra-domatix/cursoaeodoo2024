from odoo import _, api, fields, models



class SportIssueState(models.Model):
    _name = 'sport.issue.state'
    _description = 'Sport Issue State'
    
    date = fields.Date(string='Date')

    def set_done(self):
        active_ids = self.env.context.get('active_ids')
        issue = self.env['sport.issue'].browse(active_ids)
        issue.write({'date': self.date})
        issue.action_done()