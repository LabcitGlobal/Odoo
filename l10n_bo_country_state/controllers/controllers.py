# -*- coding: utf-8 -*-
# from odoo import http


# class L10nBoCountryState(http.Controller):
#     @http.route('/l10n_bo_country_state/l10n_bo_country_state/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_bo_country_state/l10n_bo_country_state/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_bo_country_state.listing', {
#             'root': '/l10n_bo_country_state/l10n_bo_country_state',
#             'objects': http.request.env['l10n_bo_country_state.l10n_bo_country_state'].search([]),
#         })

#     @http.route('/l10n_bo_country_state/l10n_bo_country_state/objects/<model("l10n_bo_country_state.l10n_bo_country_state"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_bo_country_state.object', {
#             'object': obj
#         })
