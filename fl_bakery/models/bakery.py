
from odoo import api, fields, models

class GoldenBakery(models.Model):
    _name = "golden.bakery"
    _description = "Golden Bakery"

    name = fields.Char(string='Name')
    age = fields.Integer(string='age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")

