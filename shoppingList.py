#!/usr/bin/python
# -*- encoding:utf-8 -*-
from sys import argv
import cPickle
from urllib2 import urlopen


# -----------------------------------------------------------
# --------------------- VARIABLES ---------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------

usr = ""
filepath = "./pickle"
CONFIG = "./sconfig"
password = ""
server = ""
serverPicklePath = "./sPickle"

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


try:
	config = open(CONFIG,"r")
	config.close()
except IOError:
	config = open(CONFIG,"w")
	config.close()

# -----------------------------------------------------------
# ---------------- SERVER RELATED FUNCTIONS -----------------
# -----------------------------------------------------------
# -----------------------------------------------------------

# A function for loading settings from a config file:
def getSettings(test=False):
	config = open(CONFIG,"r")
	global usr
	global password
	global server
	for setting in config:
		parts = setting.split("=")
		if parts[0] == "USER":
			usr = parts[1].rstrip("\n")
		elif parts[0] == "PASS":
			password = parts[1].rstrip("\n")
		elif parts[0] == "SERVER":
			server = parts[1].rstrip("\n")
	if (usr == "" or password == "" or server == "") and test == False:
		if usr == "":
			print "Set usr"
		if password == "":
			print "Set password"
		if server == "":
			print "Set server"
		exit()
	#TODO
	
# A function for getting the pickle from the server.
def getPickleServer():
	getSettings()
	address = server+"?who="+usr+"&pass="+password+"&cmd=REQ"
	response = urlopen(address)
	serverPickle = open(serverPicklePath,"w")
	serverPickle.write(response.read())
	serverPickle.close()
	#TODO - finish up

def makeNewConfig():
	config = open(CONFIG,"w")
	config.write("SERVER="+server+"\n")
	config.write("USER="+usr+"\n")
	config.write("PASS="+password)
	config.close()

def defineServer(name):
	getSettings(True)
	global server
	server = name
	makeNewConfig()

def defineUser(name):
	getSettings(True)
	global usr
	usr = name
	makeNewConfig()

def definePassword(name):
	getSettings(True)
	global password
	password = name
	makeNewConfig()


def printPickleServer():
	getPickleServer()
	serverPickle = open(serverPicklePath,"r")
	serverList = cPickle.load(serverPickle)
	printList(serverList)
	serverPickle.close()

def addPickleServer(item):
	getSettings()
	address = server+"?who="+usr+"&pass="+password+"&cmd=ADD&item="+item
	response = urlopen(address)
		
def removePickleServer(item):
	getSettings()
	address = server+"?who="+usr+"&pass="+password+"&cmd=REM&item="+item
	response = urlopen(address)

# -----------------------------------------------------------
# ---------------- INTERNAL FUNCTIONS -----------------------
# -----------------------------------------------------------
# -----------------------------------------------------------

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
def printList(thisList):
	for i in thisList:
		print i

# Print help menu
def printHelp():
	print "Options\n----------------\n -h or --help - displays this.\n -a  - add the following string to the shopping list. \n -r  - remove the following string  from the list, if found.\n -p or --print - prints the items currently on the list\n"
	print " --user - set username for external server\n --password - set password for external server\n --server - set server address\n"
	print " --sadd - add item to server shoppingList\n --srem - remove item from server shoppingList\n --serverList - print the list from the server\n"

# -----------------------------------------------------------
# ----------------------- MAIN BODY -------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------

def eventHandler():
	valid = False
	if len(argv) == 3:
		# If sys holds 3 arguments it will check if the second
		# hold one of the 4 commands that match.

		if(argv[1] == "-a"):
			addItem(argv[2])
			valid = True
		elif(argv[1] == "-r"):
			removeItems(argv[2])
			valid = True
		elif(argv[1] == "--sadd"):
			addPickleServer(argv[2])
		elif(argv[1] == "--srem"):
			removePickleServer(argv[2])
		elif(argv[1] == "--server"):
			defineServer(argv[2])
		elif(argv[1] == "--user"):
			defineUser(argv[2])
		elif(argv[1] == "--password"):
			definePassword(argv[2])
		else:
			printHelp()
	
		if valid:
			try:
				file = open(filepath,"w")
				cPickle.dump(list,file)
				file.close()
			except IOError:
				print "Something went wrong, when writing or opening the storage file."

	elif len(argv) == 2:
		if argv[1] == "-p" or argv[1] == "--print":
			printList(list)
		elif argv[1] == "-h" or argv[1] == "--help":
			printHelp()
		elif argv[1] == "--clear":
			clearList()	
		elif(argv[1] == "--serverList"):
			printPickleServer()
		else:
			printHelp()
	
	if len(argv) > 3:
		printHelp()

def clearList():
	file = open(filepath,"w")
	file.close();


def guiAddItem(thisX):
	list.append(thisX)
	file=open(filepath,"w")
	cPickle.dump(list,file)
	file.close()

def guiRemoveItem(thisX):
	removeItems(thisX)
	file=open(filepath,"w")
	cPickle.dump(list,file)
	file.close()

# Start eventHandler

eventHandler()
