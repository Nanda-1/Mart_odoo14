# -*- coding: utf-8 -*-
from odoo import http, models, fields
from odoo.http import request
import json
class Koboymart(http.Controller):
    @http.route('/koboymart/barang', auth='public', method=['GET'])
    def getbarang(self, **kw):
        barang = request.env['koboymart.barang'].search([])
        list =[]
        for x in barang:
            list.append({
                'nama_barang' : x.name,
                'harga_jual' : x.harga_jual,
                'stok' : x.stok
            })
            return json.dumps(list)

    @http.route('/koboymart/suppplier', auth='public', method=['GET'])
    def getsupplier(self, **kw):
        supplier = request.env['koboymart.supplier'].search([])
        list = []
        for x in supplier:
            list.append({
                'nama Perusahaan' : x.name,
                'alamat' : x.alamat,
                'no_tlpn' : x.no_telp
            })
            return json.dumps(list)

    # @http.route('/koboymart/koboymart/objects/<model("koboymart.koboymart"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('koboymart.object', {
    #         'object': obj
    #     })
