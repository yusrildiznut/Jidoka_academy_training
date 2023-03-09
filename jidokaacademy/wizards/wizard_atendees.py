# -*- coding: utf-8 -*-

from odoo import models, fields, api


class jidokaacademy(models.TransientModel):
    _name = 'wizard.atendees'

    session_id = fields.Many2one('jidokaacademy.session', string='Session')
    partner_ids = fields.Many2many('res.partner', string='Atendees')

    def process(self):
        self.session_id.partner_ids |= self.partner_ids

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
