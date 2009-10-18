#/usr/bin/env python
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

class AddAnotherGTK:

	def __init__(self):	
		#Set the Glade file
		self.gladefile = "gui.glade" 
	        self.wTree = gtk.glade.XML(self.gladefile, "winAddAnother") 
		self.wTree.signal_autoconnect(self)
		self.widget = self.wTree.get_widget
		
		self.conn = MySQLdb.connect(host = "sheeva.bsnet.se",
				       user = "bank",
			               passwd = "some_pass",
				       db = "bank")
		self.cursor = self.conn.cursor()
		
		self.widget("cmbAccount").get_model().clear()
		self.cursor.execute("SELECT AccNr FROM Account")
		res = self.cursor.fetchall()
		for row in res:
			self.widget("cmbAccount").append_text(str(row[0]))
		
	def on_cmbAccount_changed(self, widget):
		accNr = self.widget("cmbAccount").get_active_text()
		self.widget("cmbAccHolder").get_model().clear()
		self.cursor.execute("""SELECT id, name FROM AccountHolder
			     WHERE id NOT IN(select AccountHolderId
		             FROM AccountConnection WHERE AccNr = %s)""",
			     [accNr])
		res = self.cursor.fetchall()
		for row in res:
			self.widget("cmbAccHolder").append_text(str(row[0]) 							+ " - " + row[1])
		
			

	def on_btnAdd_clicked(self, widget):
		accHolder = self.widget("cmbAccHolder").get_active_text()
		accHolder = accHolder.split(" ")[0]
		accNr = self.widget("cmbAccount").get_active_text()
		self.cursor.execute("""INSERT INTO AccountConnection VALUES(
				       %s, %s)""", [accNr, accHolder])
		ToolGTK.MsgBox("Another holder added to account!")
		self.widget("winAddAnother").destroy()
