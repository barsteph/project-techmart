from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.techmart.report_supplier_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_laporan = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, supplier):
        # One sheet by partner
        sheet = workbook.add_worksheet('Daftar Supplier')
        sheet.write(0, 0, str(self.tgl_laporan))
        sheet.write(1, 0, 'Nama Perusahaan')
        sheet.write(1, 1, 'Alamat')
        sheet.write(1, 2, 'No. Telepon')
        sheet.write(1, 3, 'Produk')
        
        row = 2
        col = 0
        for obj in supplier:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col + 1, obj.alamat)
            sheet.write(row, col + 2, obj.telp)

            for item in obj.barang_supply:
                sheet.write(row, col + 3, item.name)
                col += 1
            row += 1