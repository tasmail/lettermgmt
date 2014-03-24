# -*- encoding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2013 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
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
###############################################################################

from openerp.osv import orm, fields
from openerp.tools.translate import _


class letter_folder(orm.Model):
    """Folder which contains collections of letters"""
    _name = 'letter.folder'
    _description = _('Letter Folder')
    _columns = {
        'name': fields.char('Name', required=True),
        'code': fields.char('Code', size=8, required=True),
        'letter_ids': fields.one2many('res.letter', 'folder_id', string='Letters',
                                      help='Letters contained in this folder.'),
    }
    _sql_constraints = [('code_uniq', 'unique(code)', 'Code must be unique !')]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
