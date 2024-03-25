from odoo import fields, models, api

class SportCheckIssueDone(models.TransientModel):
    _name = 'sport.check.issue.done'
    _description = 'Check Issue Done'

    date = fields.Date(string="Date")

    def check_issue_done(self):
        active_ids = self.env.context.get('active_ids')
        issues = self.env['sport.issue'].browse(active_ids)
        # issues = issues.filtered(lambda r: r.state != 'done')
        # issues = self.env['spor.issue'].search([('id', 'in', active_ids), ('state', '!=', 'done')])
        issues.write({'date': self.date})
        issues.action_done()


