from odoo.tests import common
from odoo import fields, models
from odoo.exceptions import UserError

class TestSportIssue(common.TransactionCase):
    
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.user = self.env.ref('base.user_admin')
        self.issue = self.env['sport.issue'].create({'name': 'Issue 1','state':'open'})
        self.issue_tag = self.env['sport.issue.tag'].create({'name': 'Issue 1'})

    def test_compute_assigned(self):
        self.issue.user_id = False
        # self.issue.user_id = self.user
        self.assertFalse(self.issue.assigned)
        self.issue.user_id = self.user
        self.assertTrue(self.issue.assigned)

    def test_inverse_assigned(self):
        self.issue.assigned = False
        self.assertFalse(self.issue.user_id)
        self.issue.assigned = True
        self.assertEqual(self.issue.user_id, self.env.user)
        # No puede ser self.user porque le asigna el odoo_boot
        #user 1 odoo_bot
        #user 2 admin

    def test_action_draf(self):
        # self.issue.state = 'open'
        self.issue.action_draft()
        self.assertEqual(self.issue.state,'draft')

    def test_action_done(self):
        self.issue.action_done()
        self.assertEqual(self.issue.state,'done')
        self.issue.date = False
        with self.assertRaises(UserError):
            self.issue.action_done()
        
    def test_action_fill_tags(self):
        self.issue.action_fill_tags()
        self.assertIn(self.issue.tag_ids, self.issue_tag)
