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

class AccountHolderGTK:

	def __init__(self):	
		#Set the Glade file
		self.gladefile = "gui.glade" 
	        self.wTree = gtk.glade.XML(self.gladefile, "winAccountHolder") 
		self.wTree.signal_autoconnect(self)
		self.widget = self.wTree.get_widget
		
		self.conn = MySQLdb.connect(host = "sheeva.bsnet.se",
				       user = "bank",
			               passwd = "some_pass",
				       db = "bank")
		self.cursor = self.conn.cursor()

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
		name = self.widget("txtName").get_text()
		street = self.widget("txtStreet").get_text()
		city = self.widget("txtCity").get_text()
		pin = int(self.widget("txtPin").get_text())	
		pinRetype = int(self.widget("txtPinRetype").get_text())
		if pin != pinRetype:
			ToolGTK.MsgBox("Pincodes dont match!")
			return

		self.cursor.execute("""INSERT INTO AccountHolder VALUES(
		                       null, %s, %s, %s, %s, %s)""",
				       [name, date, street, city, pin])
		ToolGTK.MsgBox("AccountHolder created!")
		self.widget("winAccountHolder").destroy()
