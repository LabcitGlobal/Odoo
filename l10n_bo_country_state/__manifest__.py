# -*- coding: utf-8 -*-
{
    'name': "Bolivian Country State",

    'summary': """
        Departments, Provinces, Municipalities for Bolivian Country State
    """,

    'description': """
        Departments, Provinces, Municipalities for Bolivian Country State.
    """,

    'author': "Labcit Inc.",
    'website': "http://www.labcit.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Localization',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
