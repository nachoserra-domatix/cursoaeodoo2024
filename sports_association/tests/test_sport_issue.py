# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests import common

class TestSportIssue(common.TransactionCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.user = self.env.ref('base.user_admin')
        self.issue = self.env['sport.issue'].create({'name':'Test Incidencia'})
    
    def test_computed_assigned(self):
        self.issue.user_id = False
        self.assertFalse(self.issue.assigned)
        self.issue.user_id = self.user
        self.assertTrue(self.issue.assigned)