from odoo import fields, models, api


class Offers(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate property offer'

    name = fields.Char(string='Price')
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')], string='Status', copy=False)
    partner_id = fields.Many2one('res.partner', required=False)
    property_id = fields.Many2one(
        'estate.property', string='Property', required=True)
    tag_ids = fields.Many2many('estate.property.tag')
    validity = fields.Integer(string='Validity', default=7)
    date_deadline = fields.Date(string='Deadline', inverse='_deadline_inverse')

    def return_action(self):
        pass
