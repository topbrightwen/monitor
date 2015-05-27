#!/usr/bin/env python

#-*- coding: utf-8 -*- 

import hostinfo_pb2
import zerorpc
import sys
 
hostinfo = hostinfo_pb2.HostInfo()
 
def ServerInfo(hostinfo):
    '''这些信息可以通过脚本进行收集'''
    hostinfo.hostname = 'cdn.oss.david.com'
    hostinfo.serverhardtype = 'IBM System x3550 M2 -[7946I1M]-'
    hostinfo.servertag = '99G0665'
    hostinfo.servertype = 'physical'
    hostinfo.gatewayIP = '113.207.61.1'
    hostinfo.serverproduct = 'IBM'
 
    cpu = hostinfo.cpus.add()
    cpu.cpuCoreNum = '1'
    cpu.cpuBit = '64'
    cpu.cpuClockSpeed = '2.00GHz'
    cpu.cpupynum = '1'
    cpu.cpuName = 'Intel Xeon'
    cpu.band = 'Intel'
    cpu.model = 'E5504'
 
    memory = hostinfo.rams.mem.add()
    memory.Serial_Number = '5F787C83'
    memory.Manufacturer = 'Samsung'
    memory.Speed = '800 MHz'
    memory.Size = '4096 MB'
 
if __name__ == "__main__":
    ServerInfo(hostinfo)
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:4242")            #连接RPC 服务端
    print c.info(hostinfo.SerializeToString())    #向服务端发送数据