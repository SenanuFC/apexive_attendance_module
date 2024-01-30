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
    'depends': ['hr_attendance', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/attendance.xml'
    ],
    # only loaded in demonstration mode
    'assets': {
        'hr_attendance.assets_public_attendance': [
            # "attendance_project/static/src/js/apexive_attendance.js",
            "attendance_project/static/src/components/project_task_form/project_task_form.js",
            "attendance_project/static/src/components/project_task_form/project_task_form.xml",
            "attendance_project/static/src/kiosk_extension/kiosk_extension.js",
            # "attendance_project/static/src/kiosk_extension/kiosk_extension.xml",
            # "attendance_project/static/src/xml/project_view_extension.xml",
            "attendance_project/static/src/xml/views.xml",
        ]
    },
}

