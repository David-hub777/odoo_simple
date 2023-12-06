from odoo import api, models, fields 

class Cliente(models.Model):
    _name = 'cliente_pedido.cliente'
    name = fields.Char(string='Nombre del Cliente')
    fecha_inicio = fields.Date()
    valoracion_pedidos = fields.Integer(string='Valoración de los Pedidos y servicio por parte del Cliente')
    
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
                raise models.ValidationError('La fecha de inicio del pedido no puede ser posterior a la fecha de entrega prevista del pedido.' + str(record.fecha_del_pedido) + ' ; '+ str(record.fecha_prevista_entrega))



class Cliente_ampliado(models.Model):
    _inherit = 'cliente_pedido.cliente'
    # _name = 'cliente_pedido.ampliandoCliente'
    numero_pedidos = fields.Integer(compute='_compute_pedidoN', store=True)
    @api.depends('pedidos')
    def _compute_pedidoN(self):
        for record in self:
            record.numero_pedidos = len(record.pedidos)
    satisfaccion_cliente = fields.Float(compute='_compute_satisfaccion', store=True) 
    @api.depends('numero_pedidos','valoracion_pedidos')
    def _compute_satisfaccion(self):
        for record in self:
            if record.numero_pedidos > 0:
                record.satisfaccion_cliente = record.valoracion_pedidos / record.numero_pedidos
            else:
                record.satisfaccion_cliente = 0.0 
