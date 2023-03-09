# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'jidokaacademy.session'
    _description = 'jidokaacademy.session'

    name = fields.Char(string='Title', required=True)
    date = fields.Date(string='Date', default=fields.Date.today())
    duration = fields.Float(string='Duration')
    seat = fields.Float('seat')
    description = fields.Text('Descripton')
    partner_id = fields.Many2one(
        'res.partner', string='Instructor', domain="[('is_instructor', '=', True)]")
    course_id = fields.Many2one(
        'jidokaacademy.course', string='Course', required=True)
    partner_ids = fields.Many2many('res.partner', string='Atendant')
    active = fields.Boolean(string='Active', default='true')

    number_of_atendant = fields.Float(compute='_compute_number_of_atendant', string='Number OF Atendant', store=True)
    
    @api.depends('partner_ids')
    def _compute_number_of_atendant(self):
        for rec in self:
            rec.number_of_atendant = len(rec.partner_ids)
        

    taken_seats = fields.Float(
        compute='_compute_taken_seats', string='Taken Seats')

    def _compute_taken_seats(self):
        for rec in self:
            if rec.partner_ids and rec.seat:
                rec.taken_seats = len(rec.partner_ids) / rec.seat * 100

            else:

                rec.taken_seats = 0

    @api.onchange('seat', 'partner_ids')
    def _onchange_seat(self):
        if self.seat < 0:

            return {
                'warning': {
                    'title': "Invalid value",
                    'message': "It was very bad indeed",
                }
            }

        elif len(self.partner_ids) > self.seat:
            return {
                'warning': {
                    'title': "Something bad happened",
                    'message': "Atenddees is overload",
                }
            }

    # @api.constrains('partner_ids', 'partner_id')
    # def _constrains_partner_id(self):
    #     for rec in self:
    #         if rec.partner_id in rec.partner_ids:
    #             raise ValidationError(
    #                 " is Instructor and cannot became attendat %s" % rec.partner_id)

    @api.constrains('partner_ids', 'partner_id')
    def _check_attendees(self):
        for record in self:
            if record.partner_id in record.partner_ids:
                raise ValidationError(
                    "Your record is too old: %s" % record.partner_id.name)


#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
