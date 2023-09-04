from odoo import models, fields

class Personal(models.Model):
    _name           = 'personal'
    _description    = 'Módulo para ejemplificar el personal de una empresa'
    categoria       = fields.Many2one('categoria', string = 'Categoria')
    codigo          = fields.Integer(string = 'Codigo')
    nombre          = fields.Char(string = 'Nombre del empleado')
    edad            = fields.Integer(string = 'Edad')

    def filtro_ver_el_personal(self):
        tree_id = self.env.ref("Modulo_personal.personal_view_tree")
        domain = ['|',('edad','<=','27'),('categoria.codigo','=','03')]
        return {
            'type': 'ir.actions.act_window',
            'name': 'Vista de personal (Con actions)',
            'view_mode': 'tree',
            'res_model': 'personal',
            'domain': domain,
            'views': [(tree_id.id, 'tree')],
            'target': 'current',
        }