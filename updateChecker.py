# -*- encoding: utf-8 -*-
from urllib2 import urlopen
adress = "https://raw.github.com/Onizuka89/shoppingList/master/"

def guiCheck(this):
	content = urlopen(adress+"guiVersion")
	if int(content.read()) == int(this):
		return 1
	elif int(content.read()) > int(this):
		return 0

def shoppingCheck(this):
	content = urlopen(adress+"shoppingListVersion")
	if int(content.read()) == int(this):
		return 1
	elif int(content.read()) > int(this):
		return 0

