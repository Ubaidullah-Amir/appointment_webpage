{
    'name': 'Appointment Webpage',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Module to create appointments via a webpage',
    'description': 'This module provides a webpage for creating appointments.',
    'author': 'Your Name',
    'depends': ['website', 'om_hospital'],
    'data': [
        'views/appointment_form.xml',
        "views/website_menu.xml",
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
