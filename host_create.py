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

f = open('json/hosts.json')
hosts = json.load(f)
pprint(hosts)
# for i in range(0, len(hosts)):
#     hosts_filter=hosts[i]
#     host_name=hosts_filter['host']
#     interface= hosts_filter['interfaces']
#     if interface != []:
#         ip = interface[0]['ip']
#         pprint(ip)
#         pprint('-----------------------')
#     else:
#         ip = '127.0.0.1'

#         zapi.host.create(host=host_name, interfaces=interface)

