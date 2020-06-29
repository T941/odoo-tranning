from odoo import models, fields


class SaleOrderTag(models.Model):
    _name = 'sale.order.tag'
    _rec_name = 'name'

    name = fields.Char("Tag")

    delivery_count = fields.Integer(string='Delivery Orders', compute='count_tag_ids')

    def count_tag_ids(self):
        count = self.env['sale.order'].search_count(
            [('tag_ids', '=', self.name)])
        self.delivery_count = count

    def action_view_delivery(self):
        action = self.env.ref('sale.action_orders').read()[0]
        action['domain'] = [('tag_ids', 'in', self.ids)]
        return action


