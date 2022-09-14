from odoo import api, fields, models


class Pegawai(models.Model):
  _name = 'techmart.pegawai'
  _description = 'Detail Pegawai'

  name = fields.Char(string='Nama')
  alamat = fields.Char(string='Alamat')
  tgl_lahir = fields.Datetime(string='Tanggal Lahir')

class Kasir(models.Model):
  _name = 'techmart.kasir'
  _inherit = 'techmart.pegawai'
  _description = 'New Description'

  id_kasir = fields.Char(string='ID Kasir')

# class CleaningService(models.Model):
#   _name = 'techmart.cleaningservice'
#   _inherit = 'techmart.pegawai'
#   _description = 'New Description'

#   id_clean = fields.Char(string='ID Cleaning Service')