#!/usr/bin/env python
#yapa-accounting: an easy to use, easy to customize accounting software for small businesses.
#Copyright (C) 2007-2008 Simon Norberg
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygtk
pygtk.require("2.0")
import gtk
import time

def InputBox(title, question, pw = False):
	dialog = gtk.Dialog(title, None, 0,
	(gtk.STOCK_OK, gtk.RESPONSE_OK,
	"Cancel", gtk.RESPONSE_CANCEL))
	hbox = gtk.HBox(False, 8)
	hbox.set_border_width(8)
	dialog.vbox.pack_start(hbox, False, False, 0)

	stock = gtk.image_new_from_stock(
		gtk.STOCK_DIALOG_QUESTION,
		gtk.ICON_SIZE_DIALOG)
	hbox.pack_start(stock, False, False, 0)
	table = gtk.Table(2, 2)
	table.set_row_spacings(4)
	table.set_col_spacings(4)
	hbox.pack_start(table, True, True, 0)
	label = gtk.Label(question)
 	label.set_use_underline(True)
	table.attach(label, 0, 1, 0, 1)
	local_entry1 = gtk.Entry()
	table.attach(local_entry1, 1, 2, 0, 1)
	label.set_mnemonic_widget(local_entry1)
	#make entry use ****
	if pw:
		local_entry1.set_visibility(False)
	dialog.show_all()
	
	response = dialog.run()
	if response == gtk.RESPONSE_OK:
		text = local_entry1.get_text()
		dialog.destroy()
		return text
	dialog.destroy()

	
def MsgBox(message):
        dialog = gtk.MessageDialog(None,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_INFO, gtk.BUTTONS_OK,
                message)
        dialog.run()
        dialog.destroy()

def YesNo(message):
        dialog = gtk.MessageDialog(None,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO,
                message)
        response = dialog.run()
        dialog.destroy()
	if response == -8:
		return "Yes"
	else:
		return "No"

def Calender():
	dialog = gtk.Dialog("Calender", None, 0,
	(gtk.STOCK_OK, gtk.RESPONSE_OK,
	"Cancel", gtk.RESPONSE_CANCEL))
	calender = gtk.Calendar()
	dialog.vbox.pack_start(calender, True, True, 0)
	dialog.show_all()
	response = dialog.run()
	if response == gtk.RESPONSE_OK:
		dialog.destroy()
		#return date as a correct datetime tuple
		tmp = calender.get_date()
		tmp2 = time.localtime()
		date = (tmp[0],tmp[1]+1,tmp[2],tmp2[3],tmp2[4],tmp2[5],tmp2[6],tmp2[7],tmp2[8])
		return date
	dialog.destroy()

def SelectComboBoxElement(cmb, name):
	model = cmb.get_model()
	iter  = model.get_iter_first()
	while iter != None:
		if model.get_value(iter, 0) == name:
			cmb.set_active_iter(iter)
			return
		iter = model.iter_next(iter)
