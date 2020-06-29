from odoo import models, fields


class Customer(models.Model):
    _inherit = "res.partner"
    cmt = fields.Char("CMT")
    _sql_constraints = [('cmt', 'UNIQUE (cmt)', 'So CMT da ton tai'), ]
