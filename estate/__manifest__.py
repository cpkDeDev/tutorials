'''
Created on 12.09.2024

@author: Peter Pulter
'''
{
    'name': 'estate',
    'depends': [
        'base'
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_menus.xml'
        ],
    'installable': True,
    'application': True
}