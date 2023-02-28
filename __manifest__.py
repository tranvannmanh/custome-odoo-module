{
    'name': 'custom_odoo_module',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        # 'data/res_country_data.xml',
        # 'data/res.country.state.csv',
        'security/ir.model.access.csv',
        'views/estate_menus.xml'
        'views/estate_property_views.xml'
    ],
    'category': 'Sales',
    'summary': 'custom module',
    'application': True,
}
