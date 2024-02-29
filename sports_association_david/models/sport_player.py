from odoo import _, api, fields, models

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    position = fields.Char()
    team_id = fields.Many2one("sport.team")
    titular = fields.Boolean(string="Titular")
    

    def add_titular(self):
        self.write({'titular' : True})

    def remove_titular(self):
        self.write({'titular' : False})