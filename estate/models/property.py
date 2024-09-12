'''
Created on 12.09.2024

@author: Peter Pulter
'''
from odoo import fields,models

class property(models.Model):
    _name = 'estate_property'
    _description = 'Estate Example Model'
    
    name = fields.Char('Name',required = True)
    postcode = fields.Char('Postcode')
    description = fields.Text('Description')
    date_availability = fields.Date('Avaiable')
    expected_price = fields.Float('Price Expected',required = True)
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('Bedrooms')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garden_area = fields.Integer('Garden Area')
    garage = fields.Boolean('Garge')
    garden = fields.Boolean('Garden')
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[
                    ('north', 'North'), 
                    ('south', 'South'), 
                    ('east', 'East'), 
                    ('west', 'West')
                    ],
        help="Ausrichtung der Hausfront")