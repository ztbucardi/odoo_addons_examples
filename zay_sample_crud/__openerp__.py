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
    'name': "Zaytech - Sample of CRUD",

    'category': 'Uncategorized',
    'version': '0.07',
    "license": "AGPL-3",
    'author': "Leandro Augusto <leandro@leandroaugusto.eti.br>",

    'website': "http://www.leandroaugusto.eti.br",
    'summary': """Addons exemplo para implementar um sistema de CRUD""",
    'description': """
        Este addons tem a estrutura base para implementar um sistema de CRUD
        """,
    'depends': ['base'],
    'data': [
        'view/sample_crud_menu.xml',
        'view/sample_crud_views.xml',
        'view/sample_crud_advanced_views.xml',
        'view/sample_crud_advanced_category_views.xml',
        'view/sample_crud_advanced_tags_views.xml',
        #'view/sample_crud_workflow.xml',
    ],
    'installable': True,
    'auto_install': True,
}
