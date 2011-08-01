#!/usr/bin/python
# -*- encoding:utf-8 -*-
import sys
import cPickle

#
# Edit to change place to store your pickle
#

filepath = "./pickle"

# Try to open file, to see if it exist, and
# if it fail it will make the file.
list = []

try:
	file = open(filepath,"r")
	list = cPickle.load(file)
	file.close()
except IOError:
	file = open(filepath,"w")
	file.close()
except EOFError:
	print "The program met an unexpected end, which probably means this is the first time running this program, or that the file is corrupted."

# List with the items to buy

# A fuction to add items to the shopping list

def addItem(x):
	list.append(x)
	print x,"is added to the shopping list"

#function to remove items
def removeItems(name_of_item):
	# Goes through list looking for a match
	# if no match found it will give a 
	# message saying that the item was 
	# not found.

	for i in list:
		if name_of_item == i:
			list.remove(name_of_item)
			print "Success"
			return True
	print "The item,",name_of_item,"was not found in the list."

# Simply prints out the items on the list.
def printList():
	print list;
	for i in list:
		print i

def printHelp():
	print "Options\n----------------\n -h or --help - displays this.\n -a  - add the following string to the shopping list. \n -r  - remove the following string  from the list, if found.\n -p or --print - prints the items currently on the list\n"

# An event handler, basicly the main body.
def eventHandler():
	valid = False
	if len(sys.argv) == 3:
		if(sys.argv[1] == "-a"):
			addItem(sys.argv[2])
			valid = True
		elif(sys.argv[1] == "-r"):
			removeItems(sys.argv[2])
			valid = True
		if valid:
			try:
				file = open(filepath,"w")
				cPickle.dump(list,file)
				file.close()
			except IOError:
				print "Something went wrong, when writing or opening the storage file."
		else:
			print "Ooops, something went wrong."
			print printHelp()

	elif len(sys.argv) == 2:
		if sys.argv[1] == "-p" or sys.argv[1] == "--print":
			printList()
		elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
			printHelp()
		elif sys.argv[1] == "--clear":
			clearList()
		else:
			printHelp()
	
	if len(sys.argv) == 1 or len(sys.argv) > 3:
		printHelp()

def clearList():
	file = open(filepath,"w")
	file.close();


# Start eventHandler

eventHandler()
