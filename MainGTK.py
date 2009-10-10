#!/usr/bin/env python
import sys
try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import gtk
  	import gtk.glade
	import gobject
except:
	sys.exit(1)

import ToolGTK
import time

class MainGTK:

	def __init__(self):	
		#Set the Glade file
		self.gladefile = "gui.glade" 
	        self.wTree = gtk.glade.XML(self.gladefile, "frmMain") 
		self.wTree.signal_autoconnect(self)
		self.widget = self.wTree.get_widget

		#fill in dates i comboBoxes
		for y in range(1901, 2001):
			self.widget("cmbYear").append_text("%02d"%y)
		for m in range(2, 13):
			self.widget("cmbMonth").append_text("%02d"%m)
		for d in range(2, 32):
			self.widget("cmbDay").append_text("%02d"%d)

	def on_btnAddAccountHolder_clicked(self, widget):
		y = self.widget("cmbYear").get_active_text()
		m = self.widget("cmbMonth").get_active_text()
		d = self.widget("cmbDay").get_active_text()
		date = y + "-" + m + "-" + d
		print date
	def on_frmMain_destroy(self, widget):
		gtk.main_quit()
	def on_btnExit_clicked(self, widget):
		gtk.main_quit()

