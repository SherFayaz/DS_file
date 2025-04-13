from odoo import models, api, fields


class OdooDeveloper(models.Model):
    _name = 'odoo.developer'


    name = fields.Char(string='Name')
    expr = fields.Integer(string='Experience')