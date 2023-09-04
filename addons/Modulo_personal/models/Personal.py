from odoo import models, fields

class Personal(models.Model):
    _name           = 'personal'
    _description    = 'Módulo para ejemplificar el personal de una empresa'
    categoria       = fields.Many2one('categoria', string = 'Categoria')
    codigo          = fields.Integer(string = 'Codigo')
    nombre          = fields.Char(string = 'Nombre del empleado')
    edad            = fields.Integer(string = 'Edad')