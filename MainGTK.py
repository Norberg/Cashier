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

import MySQLdb, time
import ToolGTK
import AccountHolderGTK
import AccountGTK
import AddAnotherGTK

class MainGTK:

	def __init__(self):	
		#Set the Glade file
		self.gladefile = "gui.glade" 
	        self.wTree = gtk.glade.XML(self.gladefile, "winMain") 
		self.wTree.signal_autoconnect(self)
		self.widget = self.wTree.get_widget
	def on_frmMain_destroy(self, widget):
		gtk.main_quit()
	def on_btnExit_clicked(self, widget):
		self.on_frmMain_destroy(widget)
	def on_btnAccountHolder_clicked(self, widget):
		AccountHolderGTK.AccountHolderGTK()
	def on_btnAddAccount_clicked(self, widget):
		AccountGTK.AccountGTK()
	def on_btnAddAnother_clicked(self, widget):
		AddAnotherGTK.AddAnotherGTK()	
