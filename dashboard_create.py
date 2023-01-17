import time
import datetime
from pyzabbix import ZabbixAPI
import urllib3
from pprint import pprint
import json

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tempo_inicial = time.time()
host = "192.168.98.200/zabbix/"
username = "matheus.carmo"
password = "Msc3275@@"
zapi = ZabbixAPI("http://" + host)
zapi.session.verify = False
urllib3.disable_warnings()
zapi.login(username, password)



f = open('json/dashboards.json')
data = json.load(f)
varredura = len(data)
for i in range(0, varredura):
    request=data[i]
    name=request['name']
    display_period= request['display_period']
    auto_start= request['auto_start']
    pages = request['pages']
    widgets= pages[0]['widgets'][0]
    userGroups= request['userGroups']
    users= request['users']
    dashboard_pageid = pages[0]['dashboard_pageid']
    zapi.dashboard.create(name=name , display_period= display_period, pages=pages)
    
    
    
    



