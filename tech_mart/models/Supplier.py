from odoo import api, fields, models


class Supplier(models.Model):
  _name = 'techmart.supplier'
  _description = 'New Description'

  name = fields.Char(string='Nama Supplier')
  alamat = fields.Char(string='Alamat')
  telp = fields.Char(string='Telepon')
  barang_supply = fields.Many2many(comodel_name='techmart.barang', string='Barang')
  
  
  
