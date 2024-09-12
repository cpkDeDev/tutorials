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
    date_availability = fields.Date('Avaiable',copy = False,default = fields.Datetime.today()) # TODO: add 3 months add()
    expected_price = fields.Float('Price Expected',required = True)
    selling_price = fields.Float('Selling Price', readonly=True,copy = False)
    bedrooms = fields.Integer('Bedrooms',default = 2)
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
    active = fields.active(active=True)
    state = fields.Selection(
        string='Status',
        selection=[
                    ('new', 'New'), 
                    ('offer_received', 'Offer Received'), 
                    ('offer_accepted', 'Offer Accepted'), 
                    ('sold', 'Sold'), 
                    ('canceled', 'Canceled')
                    ],
        help="Zustand des Angebotes")