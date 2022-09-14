from odoo import api, fields, models

class BarangDatang(models.TransientModel):
    _name = 'techmart.barangdatang'

    barang_supply = fields.Many2one(comodel_name='techmart.barang', string='Nama Barang', required=True)
    jumlah = fields.Integer(string='Jumlah', required=False)

    def button_barang_datang(self):
        for line in self:
            self.env['techmart.barang'].search([('id', '=', line.barang_supply.id)]).write(
                {'stok': line.barang_supply.stok +  line.jumlah}
            )