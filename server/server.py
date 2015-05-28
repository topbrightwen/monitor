#!/usr/bin/env python
#-*- coding: utf-8 -*- 

import miduoduo_pb2
import time,socket,threading

def tcpsession(sock,addr):
	while True:
		rawdata = sock.recv(1024)
		if rawdata == 'exit' or not rawdata:
			break
		data = miduoduo_pb2.siteinfo()
		data.ParseFromString(rawdata)
		print data.siteid
		print data.machineid
		print data.xgps
		print data.ygps
		print data.tvalue
		print data.wvalue
		sock.send('ok')
	sock.close()
	
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',4242))
s.listen(10)
	
while True:
	sock,addr = s.accept()
	t = threading.Thread(target = tcpsession,args = (sock,addr))
	t.start()
	
