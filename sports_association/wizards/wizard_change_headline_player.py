from odoo import fields, models, api, _
import logging
_logger = logging.getLogger(__name__)

class WizardChangeHeadlinePlayer(models.TransientModel):
    _name = 'wizard.change.headline.player'
    _description = 'Wizard to change the headline player'
    
    player_ids =  fields.Many2many(string=_('Player'), 
                                  comodel_name='sport.player',
                                  store=True,
                                  readonly=False,
                                  compute='_compute_players')
                                  
    def _compute_players(self):
        for record in self:
            record.write({
                'player_ids': [(6, 0, self.env.context.get('default_player_ids', []))]
            })