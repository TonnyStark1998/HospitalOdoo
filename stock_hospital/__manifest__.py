# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Module',
    'version' : '14.0.1.0.1',
    'summary': 'Visitors records in inventory',
    'category': 'Stock/hospital',
    'website': 'https://github.com/TonnyStark1998/HospitalOdoo',
    'depends' : ['base', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_hospital_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
