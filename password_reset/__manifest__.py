# -*- coding: utf-8 -*-





{
    'name': 'Password Reset',
    'version': '1.0',
    'category': 'Base',
    'summary': 'Apps will send reset password link mail to the users',
    'description': """Apps will send reset password link mail to the users.""",
    'author': 'Odoo-Valis',
    'depends': ['base', 'mail', 'auth_signup'],
    'data': [
        'views/password_cron.xml',
        'wizard/password_view.xml',
    ],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}