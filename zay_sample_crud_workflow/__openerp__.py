# -*- coding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2016 - Leandro Augusto  <leandro@leandroaugusto.eti.br>       #
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

{
    'name': "Zaytech - Workflow State of CRUD",

    'category': 'Tools',
    'version': '0.6',
    "license": "AGPL-3",
    'author': "Leandro Augusto <leandro@leandroaugusto.eti.br>",

    'website': "http://www.leandroaugusto.eti.br",
    'summary': """Addons exemplo para implementar workflow ao CRUD""",
    'description': """
        Este addons tem a estrutura base para implementar um workflow
        de state no sistema de CRUD
        """,
    'depends': ['base','zay_sample_crud'],
    'data': [
        'view/sample_crud_workflow.xml',
        'view/sample_crud_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}
