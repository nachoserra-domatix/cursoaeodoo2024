# -*- coding: utf-8 -*-
# from odoo import http


# class SportsAssociation(http.Controller):
#     @http.route('/sports_association/sports_association', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sports_association/sports_association/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sports_association.listing', {
#             'root': '/sports_association/sports_association',
#             'objects': http.request.env['sports_association.sports_association'].search([]),
#         })

#     @http.route('/sports_association/sports_association/objects/<model("sports_association.sports_association"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sports_association.object', {
#             'object': obj
#         })

