from odoo import models, fields

class SportIssue(models.Model):
    _name = "sport.issue"
    _description = "Sport Issue"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    date = fields.Date(string="Date")
    assistance = fields.Boolean(string="Assistance", help="Show if the issue needs assistance")
    state = fields.Selection(
        [("draft", "Draft"),
         ("open", "Open"),
         ("done", "Done")],
         string="State",
         default="draft",
    )

    user_id = fields.Many2one('res.users', string='User')
    sequence = fields.Integer(string='sequence')
    solution = fields.Html(string='solution')

    
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')
    tag_ids = fields.Many2many('sport.clinic', string='Clinic')

    
    


    def action_open(self):
        self.write({"state":"open"})

    def action_draft(self):
        self.write({"state":"draft"})

    def action_done(self):
        self.write({"state":"done"})
