from odoo import models, fields, api

class Categoria(models.Model):
    _name           = 'categoria'
    _description    = 'Categoria para segmentar los puestos del personal'
    codigo          = fields.Integer(string = 'Codigo')
    categoria       = fields.Char(string = 'Categoria')
    
    @api.model
    def name_get(self, id=''):
        """
            Método sobreescrito (@override) que es llamado cuando se obtienen 
            todos los registros del modelo puesto (se obtiene las tuplas de modelo
            e id del modelo) y en lugar de esto regresa un campo de texto personalizado.
        """
        result = []
        if id:
            registro = self.browse(int(id))
            name    = f"{registro.codigo or ''} - {registro.categoria or ''}"
            result.append((registro.id, name))
        else:
            for registro in self:
                name = f"{registro.codigo or ''} - {registro.categoria or ''}"
                result.append((registro.id, name))
        return result