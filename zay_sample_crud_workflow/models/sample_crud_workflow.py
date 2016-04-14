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


class ZaySampleCrudWorkflow(models.Model):
    _inherit='zay.sample.crud.advanced'

    state = fields.Selection(selection=[
        ('start', 'Start'),
        ('flow1', 'Etapa 1'),
        ('flow2', 'Etapa 2'),
        ('done',  'Done'),
        ],default='start')
