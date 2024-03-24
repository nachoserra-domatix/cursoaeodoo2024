# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields

class SportIssuesDone(models.TransientModel):
    _name ='sport.issues.done'
    _description = 'Description'
    
    date= fields.Date('Date')

    def set_done(self):
        active_ids = self.env.context.get('active_ids')
        issues = self.env['sport.issue'].browse(active_ids)
        issues.write({'date': self.date})
        issues.action_done()
    