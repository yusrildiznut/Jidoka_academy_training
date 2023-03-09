# -*- coding: utf-8 -*-

from odoo import models, fields, api


class course(models.Model):
    _name = 'jidokaacademy.course'
    _description = 'jidokaacademy.course'

    _sql_constraints = [
        ('check_name_description_constraints','CHECK (name != description)', "Name and description must be different" ),
        ('check_name_unique','UNIQUE(name)',"Name must be unique")
        
    ]

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    user_id = fields.Many2one('res.users', string='Responsible User')
    session_ids = fields.One2many('jidokaacademy.session', 'course_id', string='Sessions')

    def copy(self, default=None):
        # import pdb;
        # pdb.set_trace()
        # []

        default = dict(default or {})

        # training odoo
        # cari course name nya like copy of training odoo
        # 3

        copied_count = self.search_count (
            [('name', '=like',"Copy of {}%".format(self.name))]
        )

        # kalau tidak ada
        if not copied_count:
            # copy of training odoo
            new_name = "Copy of {}".format(self.name)
        # kalau ada
        else:
            # Copy of training odoo (jumlah ada berapa)
            new_name = "Copy of {} ({})".format(self.name,copied_count)
        
        default['name']= new_name
        # nama classnya
        return super(course, self).copy(default)
    
    # def copy(self, default=None):
    #   #  import pbd;
    #   #  pbd.set_trace()
    #   #  []
    #   default = dict(default or {})

    #   #  Training odoo
    #   #  Cari course name nya Like copy of training odoo
    #   #  3
    #   copied_count = self.search_count(
    #       [('name', '=like', "copy of {}%".format(self.name))])

    #   #  Kalau tidak ada
    #   if not copied_count:
    #      #  copy of training odoo
    #      new_name = "copy of {}".format(self.name)

    #   #  #  Kalau ada
    #   else:
    #      #  copy of training odoo (jumlah ada berapa)
    #      new_name = "copy of {} ({})".format(self.name, copied_count)

    #   default['name'] = new_name
    #   return super(Course, self).copy(default)


#
#     @api.depends('value'),
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
