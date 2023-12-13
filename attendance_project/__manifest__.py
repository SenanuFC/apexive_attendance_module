# -*- coding: utf-8 -*-
{
    'name': "attendance_project",

    'summary': "Modification of Attendance Module in Odoo for Apexive ",

    'description': """
Allow users to select a Project
Select a Project Task
Write Descriptions for their activities during both check-in and check-out
    """,

    'author': "Senanufc@yahoo.com",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_attendance', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

