# -*- coding: utf-8 -*-
# from odoo import http


# class Koboymart(http.Controller):
#     @http.route('/koboymart/koboymart/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/koboymart/koboymart/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('koboymart.listing', {
#             'root': '/koboymart/koboymart',
#             'objects': http.request.env['koboymart.koboymart'].search([]),
#         })

#     @http.route('/koboymart/koboymart/objects/<model("koboymart.koboymart"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('koboymart.object', {
#             'object': obj
#         })
