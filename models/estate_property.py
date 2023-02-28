from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Custom Estate property..."

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Boolean()
    garden_orientation = fields.Selection(
        string='Type', selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
