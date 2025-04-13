# -*- coding: utf-8 -*-
{
    'name': "galaxy hospital MSP",

    'summary': """Galaxy Hospital Management Project""",

    'description': """Galaxy Software Hospital Management project""",

    'author': "Fayaz",
    'category': 'Uncategorized',
    'version': '16.0.0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/doctor_view.xml',
        'views/patient_view.xml',
        'views/department_view.xml',
        'data/data.xml',
        'report/ir_action_report.xml',
        # 'report/patient_detail.xml',
        'report/custom_report_template.xml',
        'report/report_header.xml',
    ],

    'demo': [
        # 'demo/demo.xml',
    ],
}
