from odoo import models, fields, api

class SportIssueState(models.TransientModel):
    _name = 'sport.issue.state'
    _description = 'Set state to done'

    date = fields.Date('Date', default=fields.Date.today)

    def set_done(self):
        active_ids = self.env.context.get('active_ids')
        # issues = self.env['sport.issue'].browse(active_ids)
        # issues = issues.filtered(lambda x: x.state != 'done')
        issues = self.env['sport.issue'].search([('id','in',active_ids),('state','!=','done')])
        issues.write({'date': self.date})
        issues.action_done()