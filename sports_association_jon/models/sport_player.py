from odoo import models, fields

class SportPlayer(models.Model):
    _name = "sport.player"
    _description = "Sport Player"

    name = fields.Char(string="name")
    
    team_id = fields.Many2one(string="team",comodel_name="sport.team")
    
    age = fields.Integer(
        string="Age",
    )

    starter = fields.Boolean(
        string="Starter",
    )
    
    def starter_true(self):
        self.write({"starter":True})

    def starter_false(self):
        self.write({"starter":False})