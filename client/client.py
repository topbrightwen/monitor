#!/usr/bin/env python
#-*- coding: utf-8 -*- 

import miduoduo_pb2
import socket

sitedata = miduoduo_pb2.siteinfo()
def SiteInfo(sitedata):
	sitedata.siteid = 'demo'
	sitedata.machineid = 1
	sitedata.xgps = 110.1
	sitedata.ygps = 78.3
	sitedata.tvalue = 28
	sitedata.wvalue = 73
	sitedata.alerttime = '2015-05-28 15:41'

SiteInfo(sitedata)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('54.173.164.139',4242))
s.send(sitedata.SerializeToString())
result = s.recv(1024)
if result == 'ok':
	s.send('exit')
	print 'done'
else:
	print 'error'
s.close()



	
