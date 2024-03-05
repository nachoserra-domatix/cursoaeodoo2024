from odoo import fields, models, api , _

class SportTeam(models.Model):
    _name = 'sport.team'
    
    name = fields.Char(string=_('Name'), required=True)
    image_1920 = fields.Image(string=_('Image'), max_width=1920, max_height=1920)
    player_ids = fields.One2many(comodel_name='sport.player', inverse_name='team_id', string=_('Players'))
    sport_id = fields.Many2one(comodel_name='sport.sport', string=_('Sport'), required=True)
    trainer_id = fields.Many2one(comodel_name='res.partner', string=_('Trainer'))
    
    
    
    
    
    def action_headline_player(self):
       return {
           'name': self.name + "headlines",
           'type' : 'ir.actions.act_window',
           'view_mode': 'form',
           'res_model' : 'wizard.change.headline.player',
           'context': {'default_player_ids': self.player_ids.ids},
           'target' : 'new'
       }
            