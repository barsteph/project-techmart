from crypt import methods
import json
from odoo import http, models, fields
from odoo.http import request


class Techmart(http.Controller):
    @http.route('/techmart/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['techmart.barang'].search([])
        items = []

        for item in barang:
            items.append({
                'nama_barang': item.name,
                'harga_jual': item.harga_jual,
                'stok': item.stok
            })
        
        return json.dumps(items)

    @http.route('/techmart/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
      supplier = request.env['techmart.supplier'].search([])
      items = []

      for item in supplier:
        items.append({
            'nama_perusahaan': item.name,
            'alamat': item.alamat,
            'no_telepon': item.telp,
            'barang_id': item.barang_supply[0].name
        })

      return json.dumps(items)