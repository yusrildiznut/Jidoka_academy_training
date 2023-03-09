# -*- coding: utf-8 -*-
{
    'name': "Jidoka Academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Jidoka Team",
    'website': "https://www.jidokasystem.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/course_data.xml',
        'views/session.xml',
        'views/inheritpartner.xml',
        'views/course.xml',
        'views/views.xml',
        'views/templates.xml',
        'reports/report.xml',
        'wizards/wizard_atendees.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
