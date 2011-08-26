#!/usr/bin/python
# -*- encoding:utf-8 -*-

from Tkinter import *
import shoppingList
import updateChecker
version = 1

class Application(Frame):	

	def checkVersion(self):
		self.version = Toplevel()
		self.version.title("Version check")
		
		# First line
		self.version.description = Label(self.version, height=1, width=15)
		self.version.description["text"] = "Gui: "
		self.version.description.grid(row=0,column=0,columnspan=1)
		self.version.result = Label(self.version,height=1,width=15)
		if updateChecker.guiCheck(version) == 1:
			self.version.result["text"] = "It is up to date"
		elif updateChecker.guiCheck(version) == 0:
			self.version.result["text"] = "It is outdated"
		self.version.result.grid(row = 0, column=1, columnspan=1)

		# Second line
		self.version.description2 = Label(self.version,height=1,width=15)
		self.version.description2["text"] = "ShoppingList: "
		self.version.description2.grid(row=1,column=0,columnspan=1)
		self.version.result2 = Label(self.version,height=1,width=15)
		if updateChecker.shoppingCheck(shoppingList.version) == 1:
			self.version.result2["text"] = "It is up to date"
		elif updateChecker.shoppingCheck(shoppingList.version) == 0:
			self.version.result2["text"] = "It is outdated"
		self.version.result2.grid(column=1,row=1,columnspan=1)

	def saveSettings(self):
		shoppingList.defineServer(self.other.inputServer.get(1.0,END).strip())
		print self.other.inputServer.get(1.0,END).strip()
		shoppingList.defineUser(self.other.username.get(1.0,END).strip())
		shoppingList.definePassword(self.other.password.get(1.0,END).strip())
		shoppingList.defineChecked(self.other.var.get())
		self.updateList()

	def addToList(self):
		shoppingList.guiAddItem(self.text1.get(1.0,END).strip())
		self.updateList()

	def removeFromList(self):
		shoppingList.guiRemoveItem(self.text1.get(1.0,END).strip())
		self.updateList()
			
	# Window that appear when choosing "Connect..."
	def Preferences(self):
		self.other = Toplevel()
		self.other.title("Second Window")

		# First line
		self.other.description = Label(self.other, height=1, width=15)
		self.other.description["text"] = "Server:"
		self.other.description.grid(row=0, column=0, columnspan=1)
		shoppingList.getSettings(True)
		self.other.inputServer = Text(self.other,height=1, width=60)
		self.other.inputServer.grid(column=2, row=0, columnspan=2,padx=3,pady=3)
		self.other.inputServer.insert(INSERT,shoppingList.server)
			
		# Second line
		self.other.description2 = Label(self.other, height=1, width=15)
		self.other.description2.grid(row=1, column=0, columnspan=1)
		self.other.description2["text"] = "Username:"
		self.other.username = Text(self.other,height=1, width=60)
		self.other.username.grid(row=1, column=2, columnspan=2,padx=3,pady=3)
		self.other.username.insert(INSERT,shoppingList.usr)
		
		# Third line
		self.other.description3 = Label(self.other, height=1, width=15)
		self.other.description3.grid(row=2, column=0, columnspan=1)
		self.other.description3["text"] = "Password:"
		self.other.password = Text(self.other,height=1, width=60)
		self.other.password.grid(row=2, column=2, columnspan=2,padx=3,pady=3)
		self.other.password.insert(INSERT, shoppingList.password)
	
		# Check box	
		self.other.var = IntVar()
		self.other.checkbox = Checkbutton(self.other, text="Use?", offvalue=False,onvalue=True,variable=self.other.var)
		self.other.checkbox.grid(row=3,column=0)
		if shoppingList.checked == True:
			self.other.checkbox.select()


		# Save settings
		self.other.acceptSettings = Button(self.other)
		self.other.acceptSettings.grid(row=3, column=2)
		self.other.acceptSettings["text"] = "Save settings"
		self.other.acceptSettings["command"] = self.saveSettings		

	# Makes the menu
	def createMenu(self):
		self.menu = Menu(self)
		self.master.config(menu=self.menu)
		self.tkMenu = Menu(self.menu) 
		self.menu.add_cascade(label="ShoppingList", menu=self.tkMenu)
		self.tkMenu.add_command(label="Connect...", command=self.Preferences)	
		self.tkMenu.add_command(label="Update", command=self.checkVersion)

	def createWindow(self):
		self.createMenu()
		#settings for the grid
		shoppingList.getSettings(True)
		self.master.rowconfigure(0, weight = 1)
		self.master.columnconfigure(0, weight = 1)
		self.grid(sticky = W+E+N+S)			
		# Useless text
		self.entryLabel = Label(self, height=2, width=20)
		self.entryLabel["text"] = "Enter item name:"
		self.entryLabel.grid(column=0,row=0, rowspan=2)
	
		# Textbox with defoult content
		self.text1 = Text(self, height= 2, width=20)
		self.text1.grid(column=1, row=0, rowspan=2)
		self.text1.insert(INSERT,"mjau")	
	
		# Button to add content
		self.sendButton = Button(self)
		self.sendButton.grid(column=2,row=0)
		self.sendButton["text"] = "Add"
		self.sendButton["command"] = self.addToList
		
		# Button to remove content.
		self.deleteButton = Button(self)
		self.deleteButton.grid(column=2,row=1)
		self.deleteButton["text"] = "Remove"
		self.deleteButton["command"] = self.removeFromList
		
		# Creates a Listbox.	
		self.listbox = Listbox(self)
		self.listbox.grid(columnspan=3,rowspan=3,pady=5, ipadx=100)		
		self.updateList()	

	def addSGui(self):
		shoppingList.addPickleServer(self.text1.get(1.0,END).strip())
		self.updateList()
	
	def remSGui(self):
		shoppingList.removePickleServer(self.text1.get(1.0,END).strip())
		self.updateList()

	def updateList(self):		
		# Listbox with items
		self.listbox.delete(0,END)
		shoppingList.printPickleServer()
		if shoppingList.checked == False:	
			for i in shoppingList.list:
				self.listbox.insert(END, i)
		elif shoppingList.checked == True:
			for i in shoppingList.serverList:
				self.listbox.insert(END, i)
		if shoppingList.checked == True:
			self.sendButton["command"] = self.addSGui
		elif shoppingList.checked == False:
			self.sendButton["command"] = self.addToList		
		if shoppingList.checked == True:
			self.deleteButton["command"] = self.remSGui
		elif shoppingList.checked == False:
			self.deleteButton["command"] = self.removeFromList

	
	def __init__(self, master=None):
		
		Frame.__init__(self, master)
		self.pack()
		self.createWindow()
root = Tk()
app = Application(master = root)
app.mainloop()
#root.destroy()
