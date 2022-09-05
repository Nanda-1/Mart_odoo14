from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'koboymart.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('makananbasah', 'Makanan Basah'), 
        ('makanankering', 'Makanan Kering'), 
        ('minuman', 'Minuman'),
        ('bahanmakananbasah', 'Bahan Makanan Basah'),
        ('bahanmakanankering', 'Bahan Makanan kering')        
    ], string='Nama Kelompok')

    kode_kelompok = fields.Char(string='Kode Kelompok')
    
        
    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if (self.name == 'makananbasah'):
            self.kode_kelompok = 'mak01'
        elif (self.name == 'makanankering'):
            self.kode_kelompok = 'mak02'
        elif (self.name == 'minuman'):
            self.kode_kelompok = 'min'
        elif (self.name == 'bahanmakananbasah'):
            self.kode_kelompok = 'bhnmak01'
        elif (self.name == 'bahanmakanankering'):
            self.kode_kelompok = 'bhnmak02'

    kode_rak = fields.Char(string='Kode Rak')
    barang_ids = fields.One2many(comodel_name='koboymart.barang', 
                                inverse_name='kelompokbarang_id', 
                                string='Daftar Barang')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['koboymart.barang'].search([('kelompokbarang_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

    daftar = fields.Char(string='Daftar Isi')