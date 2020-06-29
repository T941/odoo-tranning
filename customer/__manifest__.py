{
    'name': 'Sales_SK',
    'category': 'Sales',
    'author': 'SK',
    'depends': [
        'base','sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_view.xml',
        'views/menu_sale_order.xml',
        'views/sale_order_tag_views.xml'
    ],
    'installable': True,
    'application': True,

}
