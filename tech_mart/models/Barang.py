from odoo import api, fields, models


class Barang(models.Model):
  _name = 'techmart.barang'
  _description = 'Produk-produk Elektronik Komputer'

  name = fields.Char(string='Name')
  seri = fields.Char(string='Seri')

  harga_modal = fields.Integer(string='Harga Modal',required=True)
  harga_jual = fields.Integer(string='Harga Jual', required=True)

  kelompok_id = fields.Many2one(comodel_name='techmart.kelompokbarang',
                                string='Kategori Produk',
                                ondelete='cascade')

  supplier_id = fields.Many2many(comodel_name='techmart.supplier',
                                 string='Supplier')
                                 
  stok = fields.Integer(string='Stok')
  
  
  
