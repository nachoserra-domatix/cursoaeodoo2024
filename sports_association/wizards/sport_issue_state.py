from odoo import models, fields, api, Command, _
#from datetime import date


class SportIssueState(models.TransientModel):
    _name = 'sport.issue.state'
    _description = "Set state to done"

    date = fields.Date('Date')

    def set_done(self):
        active_ids = self.env.context.get('active_ids')
        
        issues = self.env['sport.issue'].browse(active_ids)
        
        issues.write({'date': self.date})
        issues.action_done()

