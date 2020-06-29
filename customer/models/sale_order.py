from odoo import models,fields,api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    tag_ids = fields.Many2many('sale.order.tag',string='Tag ID')






