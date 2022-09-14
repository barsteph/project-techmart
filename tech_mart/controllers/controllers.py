# -*- coding: utf-8 -*-
# from odoo import http


# class TechMart(http.Controller):
#     @http.route('/tech_mart/tech_mart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_mart/tech_mart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_mart.listing', {
#             'root': '/tech_mart/tech_mart',
#             'objects': http.request.env['tech_mart.tech_mart'].search([]),
#         })

#     @http.route('/tech_mart/tech_mart/objects/<model("tech_mart.tech_mart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_mart.object', {
#             'object': obj
#         })
