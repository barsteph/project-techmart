from odoo import api, fields, models


class KelompokBarang(models.Model):
  _name = 'techmart.kelompokbarang'
  _description = 'Kategori produk-produk Elektronik Komputer'

  # name = fields.Char(string='Kategori')
  name = fields.Selection([
    ('notebook asus', 'Notebook ASUS'),
    ('notebook lenovo', 'Notebook Lenovo')
  ], string='Kategori')


  kode_kelompok = fields.Char(string='Kode Kategori')

  @api.onchange('name')
  def _onchange_kelompok(self):
    if (self.name == 'notebook asus'):
      self.kode_kelompok = "NAs"
    elif (self.name == 'notebook lenovo'):
      self.kode_kelompok = 'NLen' 

  barang_ids = fields.One2many(comodel_name='techmart.barang',
                               inverse_name='kelompok_id', 
                               string='Daftar Barang')

  jml_barang = fields.Char(compute='_compute_jml_barang', string='Jumlah')
  
  @api.depends('barang_ids')
  def _compute_jml_barang(self):
    for rec in self:
      a = self.env['techmart.barang'].search([('kelompok_id', '=', rec.id)]).mapped('name')
      b = len(a)
      rec.jml_barang = b
      rec.daftar = a

  daftar = fields.Char(string='Daftar Isi')
  
  

