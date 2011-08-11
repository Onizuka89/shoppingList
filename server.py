# -*- encoding:utf8 -*-
from mod_python import util
from mod_python import apache
import re
import cPickle
from os.path import abspath
def handler(req):
	req.log_error('handler')
	req.content_type = "text/plain"
	req.send_http_header()
	PICKLE ="/home/studenter/it09/stiansd/htdocs/python/pickle"
	CONFIG = "/home/studenter/it09/stiansd/htdocs/python/config.cfg"
	form = util.FieldStorage(req,keep_blank_values=4)
	who = form.get("who",None)
	password = form.get("pass",None)
	request = form.get("cmd",None)
	item = form.get("item",None)
	try:
		config = open(CONFIG,"r")
	except IOError:
		config = open(CONFIG,"w")		
	user = ""
	Password = ""
	
	for everyLine in config:
		parts = everyLine.split(":")
		temp = re.split("\n$",parts[1])
		parts[1] = temp[0]
		if parts[0] == "USER":
			user = parts[1]
		elif parts[0] == "PASS":
			Password = parts[1]	
	
	if who == user and Password == password:
		if request == "REQ":
			file = open(PICKLE,"r")
			req.write(str(cPickle.load(file)))
			file.close()
			return apache.OK
		elif request == "ADD" or request == "REM":
			req.write("okay 1 \n")
			if item != None:
				req.write("okay 2\n")
				file = open(PICKLE,"r")
				list = cPickle.load(file)
				if request == "ADD":
					list.append(unicode(str(item)))
				elif request == "REM":
					for i in list:
						if i == item:
							list.remove(unicode(str(item)))
				file.close()
				file = open(PICKLE,"w")
				cPickle.dump(list,file)
				file.close()
	return apache.OK
