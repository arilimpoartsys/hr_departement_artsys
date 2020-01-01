# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'HR Department Advances',
    'version': '1.0',
    'summary': 'Add some fields for Organization Structure',
    'description': """
          add some fields :.
          Directorate,
          Division,
          Department,
          Unit,
          Sub Unit,
    """,

    'company': "PT. Artsys Integrasi Solusindo",
    'author': "PT. Artsys Integrasi Solusindo",
    'maintainer': "PT. Artsys Integrasi Solusindo",
    'website': "http://www.artsys.id",
    'category': 'HRMS - Human Resource Management System',
    'depends': ['hr'],
    'data': [
        'views/hr_views.xml',
        'views/hr_department_views.xml',
    ],
    'css': [],
    'qweb': [],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
}
