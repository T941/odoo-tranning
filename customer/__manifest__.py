{
    'name': 'Sales_SK',
    'category': 'Sales',
    'author': 'SK',
    'depends': [
        'base','sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/inherit_view.xml',
        'views/sale_order_tag_view.xml',

    ],
    'installable': True,
    'application': True,

}
