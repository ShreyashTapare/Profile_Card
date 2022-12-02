# -*- coding: utf-8 -*-
{
    'name': "Portal_Profile",

    'summary': """
        Just Basic Module Which Adds extra Detail Field In Profile Section.
        
        """,

    'description': """
        Just Basic Module Which Adds extra Detail Field In Profile Section.
        To Install Just Drag And Drop This Zip File Inside Odoo Addon Folder And Search Name Without App Filter And Install And You Are Done.
    """,

    'author': "Shreyash Tapare",
    'website': "http://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        'views/views.xml'

    ],

    'license': 'LGPL-3',
}
