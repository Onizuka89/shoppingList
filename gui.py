#!/usr/bin/python
# -*- encoding:utf-8 -*-

from Tkinter import *
import shoppingList

class Application(Frame):	
	def addToList(self):
		shoppingList.guiAddItem(self.text1.get(1.0,END).strip())
		shoppingList.printList()
	
	def removeFromList(self):
		shoppingList.guiRemoveItem(self.text1.get(1.0,END).strip())
		shoppingList.printList()
			
	def displayText(self):
		shoppingList.printList()
	
	def createWindow(self):
		self.master.rowconfigure(0, weight = 1)
		self.master.columnconfigure(0, weight = 1)
		self.grid(sticky = W+E+N+S)
	
		self.entryLabel = Label(self, height=2, width=20)
		self.entryLabel["text"] = "Enter item name:"
		self.entryLabel.grid(column=0,row=0, rowspan=2)
	
		self.text1 = Text(self, height= 2, width=20)
		self.text1.grid(column=1, row=0, rowspan=2)
		self.text1.insert(INSERT,"mjau")	
	
		self.sendButton = Button(self)
		self.sendButton.grid(column=2,row=0)
		self.sendButton["text"] = "Add"
		self.sendButton["command"] = self.addToList
		

		self.deleteButton = Button(self)
		self.deleteButton.grid(column=2,row=1)
		self.deleteButton["text"] = "Remove"
		self.deleteButton["command"] = self.removeFromList
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWindow()

root = Tk()
app = Application(master = root)
app.mainloop()
root.destroy()
