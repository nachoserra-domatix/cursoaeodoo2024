from odoo.tests import common
from odoo import fields,models
from odoo.exceptions import UserError

class TestSportsIssue(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.issue = self.env['sports.issue'].create({'name':'Test issue','description':'Test description','state':'open'})
        self.issue2 = self.env['sports.issue'].create({'name':'Test issue 2','description':'Test description','state':'open'})
        self.user_id = self.env.ref('base.user_admin')
        self.tag = self.env['sports.issue.tag'].create({'name':'Test issue'})
    
    def test_compute_asigned(self):
        self.issue.user_id = False
        self.assertFalse(self.issue.assigned)
        import pdb; pdb.set_trace()
        self.issue.user_id = self.user_id
        self.assertTrue(self.issue.assigned)
    
    def test_inverse_assigned(self):
        self.issue.assigned = False
        self.assertFalse(self.issue.user_id)
        self.issue.assigned = True
        self.assertEqual(self.issue.user_id,self.env.user)
    
    def test_action_draft(self):
        self.issue.action_draft()
        self.assertEqual(self.issue.state,'draft')  
    
    def test_action_done(self):
        import pdb; pdb.set_trace()
        self.issue.action_done()
        self.assertEqual(self.issue.state,'done')
        self.issue.date =False
        with self.assertRaises(UserError):
            self.issue.action_done()
    
    def test_action_add_tag(self):
        self.issue.action_add_tag()
        self.assertEqual(self.issue.tag_ids,self.tag)
        self.issue2.action_add_tag()
        self.assertIn(self.issue2.name,self.issue2.tag_ids.mapped('name'))

    

