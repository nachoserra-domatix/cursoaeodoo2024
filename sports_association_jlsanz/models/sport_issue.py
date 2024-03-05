from odoo import models, fields, api

class SportIssue(models.Model):
    _name = 'sport.issue'
    _description = 'Sport Issue'

    name = fields.Char(string='Name')
    description = fields.Text(string='Desciption')
    date = fields.Date(string='Date')
    assistance = fields.Boolean(string='Assistance', help="Show")
    state = fields.Selection(
        [('draft', 'Draft'),
         ('open', 'Open'),
         ('done', 'Done')],
        string='State',
        default='draft'
    )

    user_id = fields.Many2one('res.users', string="User")
    sequence = fields.Integer(string="Sequence", default="10")
    solution = fields.Html(string="Solutions")
    color = fields.Integer(string="Color", default=0)
    cost = fields.Float(string="cost")

    assigned = fields.Boolean(string='Assigned', compute='_compute_assigned', inverse='_inverse_assigned')

    clinic_ids= fields.Many2one('sport.clinic', string='Clinic')

    tag_ids = fields.Many2many('sport.issue.tag', string='Tags')

    #user_phone = fields.Char(string='User_phone', related='uiser_id.phone', store=True. readonly=False)

    #@api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    def _inverse_assigned(self):
            for record in self:
                if record.assigned:
                    record.user_id = False
                else:
                    record.user_id = self.env.user

    #def _search_assigned(self):

    def action_open(self):        
        for record in self:
            record.state = 'open'

    def action_draft(self):        
        for record in self:
            record.state = 'draft'

    def action_done(self):        
        for record in self:
            #record.state = 'done'
                record.write()

#    def action.open_all_issues(self):
#        for record in self:
#            action.open(record)

    def action_add_tags_like_name(self):
        for record in self:
                result_tags = self.env['sport.issue.tag'].search([('name', 'ilike', record.name)])
                #import pdb; pdb.trace();
                if result_tags:
                    record.tag_ids = [(6,0,result_tags.ids)]
                else:
                    record.tag_ids = [(0,0,{'name':record.name})]
