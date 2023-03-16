from odoo import models, fields, api


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
    garden_area = fields.Float()
    garden_orientation = fields.Selection(
        string='Type', selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])
    property_type_id = fields.Many2one('estate.property.type')
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    saleperson = fields.Many2one(
        'res.users', string='Saleperson', default=lambda self: self.env.user)
    tags_id = fields.Many2many(
        'estate.property.tag', string='Tag', required=False)
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    total_area = fields.Float(String='Total Area', compute='_total_area')

    @api.depends('garden_area', 'living_area')
    def _total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
