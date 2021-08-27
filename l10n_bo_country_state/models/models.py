# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class l10n_bo_country_state(models.Model):
#     _name = 'l10n_bo_country_state.l10n_bo_country_state'
#     _description = 'l10n_bo_country_state.l10n_bo_country_state'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
