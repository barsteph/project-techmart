from odoo import api, fields, models


class ResPartner(models.Model):
  _inherit = 'res.partner'
  _description = 'New Description'

  is_konsumen = fields.Boolean(string='Adalah Konsumen')
  # is_direksi = fields.Boolean(string='Adalah Direksi')
  poin = fields.Integer(string='Poin')
  level = fields.Char(string='Level')
