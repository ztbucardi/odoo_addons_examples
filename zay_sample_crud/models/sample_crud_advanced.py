# -*- coding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2016 - Leandro Augusto  <leandro@leandroaugusto.eti.br>       #
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).               #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

from openerp import models, fields, api

import logging
_logger = logging.getLogger(__name__)


class ZaySampleCrudAdvanced(models.Model):
    _name='zay.sample.crud.advanced'

    # Exemplo de campos simples
    name = fields.Char( string = 'Nome')
    summary = fields.Text()
    description = fields.Html()
    active = fields.Boolean(string = 'Ativo ?')
    position = fields.Integer()
    value = fields.Float()
    photo = fields.Binary()
    classification = fields.Selection(selection=[('class1', 'Class 1'), ('class2', 'Class 2') ])
    category = fields.Many2one("zay.sample.crud.advanced.category", "Category")
    tags =  fields.Many2many(comodel_name='zay.sample.crud.advanced.tags',
                             relation='zay_sample_crud_advanced_tags_rel',
                             column1='crud_id',column2='tags_id', string="Tags")


    # Exemplo de campos avancado
    #aselection = fields.Selection(selection='a_function_name')
    #...
