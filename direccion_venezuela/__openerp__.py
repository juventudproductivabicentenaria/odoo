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
#
{
    'name': 'Direccion Venezuela',
    'version': '1.0',
    'depends': ['base','sale'],
    'author': 'Jeison Pernía (Comunidad Bachaco.ve)',
    'category': 'Configuración Técnica',
    'description': """
    Este módulo crea el formato para una direeción en Venezuela de un cliente:
        
        
        Dirección
            
            Estado
            
            Municipio
            
            Parroquia
            
            Sector
            
            Calle / Avenida
            
            Casa /Edificio
            
            Piso y Apartamento
            """,
    'update_xml': [],
    "data" : [
        'company_venezuela_view.xml',
        'direccion_venezuela_view.xml',
        'partner_venezuela_view.xml',
        'sale_venezuela.xml',
        'data/estados.xml',
        'data/municipios.xml',
        'data/parroquias.xml',
       
        ],
    'installable': True,
    'auto_install': False,
}

