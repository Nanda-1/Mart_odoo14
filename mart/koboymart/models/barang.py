from odoo import api, fields, models


class Barang(models.Model):
    _name = 'koboymart.barang'
    _description = 'New Description'

    name = fields.Char(string='Nama Barang')
    harga_beli = fields.Integer(string='Harga Modal',required=True)
    harga_jual = fields.Integer(string='Harga Jual',required=True)
    kelompokbarang_id = fields.Many2one(comodel_name='koboymart.kelompokbarang', 
                                        string='Kelompok Barang',
                                        ondelete='cascade')
    supplier_id = fields.Many2many(comodel_name='koboymart.supplier', string='Supplier')
    stok = fields.Integer(string='Stok')

    