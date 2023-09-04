from odoo import models, fields

class Categoria(models.Model):
    _name           = 'categoria'
    _description    = 'Categoria para segmentar los puestos del personal'
    codigo          = fields.Integer(string = 'Codigo')
    categoria       = fields.Char(string = 'Categoria')