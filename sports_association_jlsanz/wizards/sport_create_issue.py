from odoo import fields, api, models

class SportCreateIssue(models.TransientModel):
    _name = 'sport.create.issue'
    _description = 'Create Issue'

    name = fields.Char('Issue Name')
    #clinic_id = fields.Many2one('sport.clinic', string='Clinic', default=lambda self: self.env.context.get('active_id'))
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')
    player_id = fields.Many2one('sport.player', string='Player')

    def create_issue(self):
        # Se puede diferenciar por el método que lo ha llamado
        #active_id = self.env.context('active_id')
        #if self.env.context('active_model') == 'sport.clinic':
        #   clinic = self.env['sport.clinic'].browse(active_id)
        #   self.clinic_ids = clinic.id
        vals = {
            'name': self.name,
            'clinic_ids': self.clinic_id.id,
            'player_id': self.player_id.id,
            }
        issue = self.env['sport.issue'].create(vals)
        # Devolver el formulario del registro creado
        return {
            'name': 'Issue',
            'view_mode': 'form',
            'res_model': 'sport.issue',
            'res_id': issue.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }