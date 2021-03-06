# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia !
from openerp.osv import fields, osv

class partner_venezuela(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    
    def limpiar_campos(self,cr,uid,ids,nombre):
        res={}
        if nombre=='estado':
            res={
            'municipio_id':'',
            'parroquia_id':'',
            
                }
        if nombre=='municipio':
            res={
            'parroquia_id':'',
            
                }
        return {
         'value':res
            }
    def _default_venezuela(self,cr,uid,ids,context=None):
        res={}
        country_obj=self.pool.get('res.country')
        country_id=country_obj.search(cr,uid,[('name','=','Venezuela')],context=context)
        return country_id[0]
    
    
    _columns = {
        'estado_id': fields.many2one('direccion.ven.estados',
                    'Estado',
                    #~ required=True,
                    help='Estado donde vive el usuario'),
        'municipio_id': fields.many2one('direccion.ven.municipios',
                    'Municipio',
                    #~ required=True,
                    help='Municipio donde vive el usuario'),
        'parroquia_id': fields.many2one('direccion.ven.parroquias',
                    'Parroquia',
                    #~ required=True,
                    help='Parroquia donde vive el usuario'),
        'sector': fields.char('Sector',
                    size=80,
                    help='Sector donde vive el usuario'
                    ),
        'calle_av': fields.char('Calle/Avenida',
                    size=80,
                    help='Calle/Avenida donde vive el usuario'
                    ),
        'casa_edif': fields.char('Casa/Edificio',
                    size=80,
                    help='Casa/Edificio donde vive el usuario'
                    ),
        'piso_apart': fields.char('Piso y Apartemento',
                    size=20,
                    help='Piso y Apartemento donde vive el usuario'
                    ),
        'pers_nat': fields.boolean('Persona Natural', help="Marcar si el contacto es una persona natural"),
        'agent_ret': fields.boolean('Agente de Retencion IVA', help="Marcar si el contacto es un agente de rención IVA"),
        'select_agent_ret':fields.selection([('0', '0%'),('75', '75%'),('100', '100%')],'Seleccionar_%_agente_retencion' ),
        'islr': fields.boolean('ISLR', help=" Retención de Impuesto Sobre La Renta"),
        'select_islr':fields.selection([('1', 'Pagar Muchooo'),('2', 'Pagar Todo'),('3', 'Pagar 10%')],'seleccionar_retencion_IVA' ),
        'select_tipo_ced':fields.selection([('1', 'V-'),('2', 'E-')],'seleccionar_tipo_cedula' ),
        'cedula': fields.char('Cédula', help="Cedula de Persona Natural"),
        'select_tipo_rif':fields.selection([('1', 'J-'),('2', 'V-'),('3', 'G-'),('4', 'E-')],'seleccionar_tipo_cedula' ),
        'rif': fields.char('RIF', help="RIF de Persona Jurídica ó Natural"),
        
        
    }
    
    _defaults = {
        'country_id':_default_venezuela,
        'select_tipo_ced':'1',
        'select_tipo_rif':'1',
        
    }

    
class ubicacion_mapa(osv.osv):

    _inherit = "res.partner"

    def open_map(self, cr, uid, ids, context=None):
        address_obj= self.pool.get('res.partner')
        partner = address_obj.browse(cr, uid, ids, context=context)[0]
        url="http://maps.google.com/maps?oi=map&q="
        
        if partner.casa_edif:
            url+='+'+partner.casa_edif.replace(' ','+')
        if partner.calle_av:
            url+='+'+partner.calle_av.replace(' ','+')
        if partner.sector:
            url+='+'+partner.sector.replace(' ','+')
        if partner.parroquia_id:
            url+='+'+partner.parroquia_id.parroquia.replace(' ','+')
        if partner.municipio_id:
            url+='+'+partner.municipio_id.municipio.replace(' ','+')
        if partner.estado_id:
            url+='+'+partner.estado_id.estado.replace(' ','+')
        if partner.country_id:
            url+='+'+partner.country_id.name.replace(' ','+')
        if partner.street:
            url+=partner.street.replace(' ','+')
        if partner.city:
            url+='+'+partner.city.replace(' ','+')
        if partner.state_id:
            url+='+'+partner.state_id.name.replace(' ','+')
        if partner.zip:
            url+='+'+partner.zip.replace(' ','+')
        return {
        'type': 'ir.actions.act_url',
        'url':url,
        'target': 'new'
        }

ubicacion_mapa()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4
