from odoo import api, models, fields 

class Cliente(models.Model):
    _name = 'cliente_pedido.cliente'
    name = fields.Char(string='Nombre del Cliente')
    fecha_inicio = fields.Date()
    pedidos = fields.One2many('cliente_pedido.pedido', 'cliente_id', string='Pedidos del Cliente')

class Pedido(models.Model):
    _name = 'cliente_pedido.pedido'
    name = fields.Char(string='Número de Pedido')
    cliente_id = fields.Many2one('cliente_pedido.cliente', string='Cliente')
    fecha_del_pedido = fields.Date()
    fecha_prevista_entrega = fields.Date()
    @api.constrains('fecha_del_pedido', 'fecha_prevista_entrega')
    def _check_dates(self):
        for record in self:
            if record.fecha_del_pedido > record.fecha_prevista_entrega:
                raise models.ValidationError('La fecha de inicio del pedido no puede ser posterior a la fecha de entrega prevista del pedido.')




