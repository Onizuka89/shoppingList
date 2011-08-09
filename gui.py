#!/usr/bin/python
# -*- encoding:utf-8 -*-

from Tkinter import *
import shoppingList


class Application(Frame):	
	
	
	def addToList(self):
		shoppingList.guiAddItem(self.text1.get(1.0,END).strip())
		self.updateList()

	def removeFromList(self):
		shoppingList.guiRemoveItem(self.text1.get(1.0,END).strip())
		self.updateList()
			
	# Window that appear when choosing "Connect..."
	def Preferences(self):
		other = Toplevel()
		other.title("Second Window")
		other.description = Label(other, height=2, width=20)
		other.description["text"] = "Enter server name:"
		other.description.grid(row=0, column=0, columnspan=2)
	
	# Makes the menu
	def createMenu(self):
		self.menu = Menu(self)
		self.master.config(menu=self.menu)
		self.tkMenu = Menu(self.menu) 
		self.menu.add_cascade(label="Tkmenu", menu=self.tkMenu)
		self.tkMenu.add_command(label="Connect...", command=self.Preferences)	
	
	def createWindow(self):
		self.createMenu()
		#settings for the grid
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

	def updateList(self):		
		# Listbox with items
		self.listbox.delete(0,END)
		for i in shoppingList.list:
			self.listbox.insert(END, i)
	
	def __init__(self, master=None):
		
		Frame.__init__(self, master)
		self.pack()
		self.createWindow()

root = Tk()
app = Application(master = root)
app.mainloop()
#root.destroy()
