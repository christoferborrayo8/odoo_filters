from odoo import models, fields

class ResUsers(models.Model):
    _inherit    = 'res.users'
    categoria   = fields.Many2one('categoria', string = 'Categoria')