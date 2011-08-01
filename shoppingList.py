#!/usr/bin/python
# -*- encoding:utf-8 -*-
import sys

# List with the items to buy
list = []

# A fuction to add items to the shopping list

def addItem(x):
	list.append(x)
	print x,"is added to the shopping list"

# Function to remove items
def removeItems(name_of_item):
	# Goes through list looking for a match
	# if no match found it will give a 
	# message saying that the item was 
	# not found.
	for i in list:
		if name_of_item == i:
			list.remove(name_of_item)
			return True
	print "The item,",name_of_item,"was not found in the list."

# Simply prints out the items on the list.
def printList():
	for i in list:
		print i

def printHelp():
	print "Options\n----------------\n -h or --help - displays this.\n -a  - add the following string to the shopping list. \n -r  - remove the following string  from the list, if found.\n -p or --print - prints the items currently on the list\n"

# An event handler, basicly the main body.
def eventHandler():
	if len(sys.argv) == 3:
		if(sys.argv[1] == "-a"):
			addItem(sys.argv[2])
		elif(sys.argv[1] == "-r"):
			removeItems(sys.argv[2])
	elif len(sys.argv) == 2:
		if sys.argv[1] == "-p" or sys.argv[1] == "--print":
			printList()
		elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
			printHelp()

	
# Temporary testing lines
addItem("Jimmy Hendrix")

# Start eventHandler

eventHandler()
