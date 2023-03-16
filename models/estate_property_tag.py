from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Tags for estates'

    name = fields.Char(string='Tag', required=True)
    partner_id = fields.Many2one('res.partner', required=False)
