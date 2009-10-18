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

class AccountGTK:

	def __init__(self):	
		#Set the Glade file
		self.gladefile = "gui.glade" 
	        self.wTree = gtk.glade.XML(self.gladefile, "winAccount") 
		self.wTree.signal_autoconnect(self)
		self.widget = self.wTree.get_widget
		
		self.conn = MySQLdb.connect(host = "sheeva.bsnet.se",
				       user = "bank",
			               passwd = "some_pass",
				       db = "bank")
		self.cursor = self.conn.cursor()
		
		self.cursor.execute("SELECT id, name FROM AccountHolder")
		res = self.cursor.fetchall()
		for row in res:
			self.widget("cmbAccountHolder").append_text(str(row[0]) 							+ " - " + row[1])
		
	def on_btnCreateAccount_clicked(self, widget):
		accHolder = self.widget("cmbAccountHolder").get_active_text()
		accHolder = accHolder.split(" ")[0]
		self.cursor.execute("""INSERT INTO Account VALUES(
		                       null, %s)""",["0"])
		self.cursor.execute("""INSERT INTO AccountConnection VALUES(
				       (select max(AccNr) from Account), %s)"""
					, [accHolder])
		ToolGTK.MsgBox("Account created!")
		self.widget("winAccount").destroy()
