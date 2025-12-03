# -*- coding: utf-8 -*-
{
    'name': "Gestion Entreprise",
    'summary': "Gestion des groupes d'entreprises et des entreprises",
    'description': """
        Module de gestion des entreprises
        ==================================
        * Groupes d'entreprises
        * Entreprises
        * Salariés rattachés aux entreprises
    """,
    'author': "MoonDev",
    'version': '1.0',
    'category': 'Business',
    'depends': ['base', 'gestion_ecole'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}
