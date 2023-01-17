import time
import datetime
from pyzabbix import ZabbixAPI
import urllib3
from pprint import pprint
import json

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tempo_inicial = time.time()
host = "192.168.21.76"
username = "rta.ancine"
password = "rt@.@nc1n3I0$"
zapi = ZabbixAPI("http://" + host)
zapi.session.verify = False
urllib3.disable_warnings()
zapi.login(username, password)


# Testando todos os metodos da API que tem como opção create with API

dashboards = zapi.dashboard.get(output="extend", selectPages="extend", selectUsers="extend", selectUserGroups="extend")
graphs = zapi.graph.get(output="extend")
graphs_prototypes = zapi.graphprototype.get(output="extend")
hosts = zapi.host.get(selectParentTemplates='extend', output='extend', selectInterfaces='extend')
hosts_groups = zapi.hostgroup.get(output="extend")
hosts_interface = zapi.hostinterface.get(output="extend")
iconmap = zapi.iconmap.get(output='extend')
image = zapi.image.get(output='extend')
map_ = zapi.map.get(output='extend')
media_type = zapi.mediatype.get(output='extend')
proxy = zapi.proxy.get(output='extend')
report = zapi.report.get(output='extend')
scripts = zapi.script.get(output='extend')
service = zapi.service.get(output='extend')
settings = zapi.settings.get(output='extend')
sla = zapi.sla.get(output='extend')
role = zapi.role.get(output='extend')
token = zapi.token.get(output='extend')
trigger = zapi.trigger.get(output='extend')
trigger_prototype = zapi.triggerprototype.get(output='extend')
user = zapi.user.get(output='extend')
user_group = zapi.usergroup.get(output='extend')
user_macro = zapi.usermacro.get(output='extend')
value_map = zapi.valuemap.get(output='extend')
web_services = zapi.httptest.get(output='extend')



with open('json/dashboards.json', 'w') as f:
    json.dump(dashboards, f)
with open('json/graphs.json', 'w') as f:
    json.dump(graphs, f)
with open('json/graphs_prototypes.json', 'w') as f:
    json.dump(graphs_prototypes, f)
with open('json/hosts.json', 'w') as f:
    json.dump(hosts, f)
with open('json/hosts_groups.json', 'w') as f:
    json.dump(hosts_groups, f)
with open('json/hosts_interface.json', 'w') as f:
    json.dump(hosts_interface, f)
with open('json/iconmap.json', 'w') as f:
    json.dump(iconmap, f)
with open('json/image.json', 'w') as f:
    json.dump(image, f)
with open('json/map_.json', 'w') as f:
    json.dump(map_, f)
with open('json/media_type.json', 'w') as f:
    json.dump(media_type, f)
with open('json/proxy.json', 'w') as f:
    json.dump(proxy, f)
with open('json/report.json', 'w') as f:
    json.dump(report, f)
with open('json/scripts.json', 'w') as f:
    json.dump(scripts, f)
with open('json/service.json', 'w') as f:
    json.dump(service, f)
with open('json/settings.json', 'w') as f:
    json.dump(settings, f)
with open('json/sla.json', 'w') as f:
    json.dump(sla, f)
with open('json/role.json', 'w') as f:
    json.dump(role, f)
with open('json/token.json', 'w') as f:
    json.dump(token, f)
with open('json/trigger.json', 'w') as f:
    json.dump(trigger, f)
with open('json/trigger_prototype.json', 'w') as f:
    json.dump(trigger_prototype, f)
with open('json/user.json', 'w') as f:
    json.dump(user, f)
with open('json/user_group.json', 'w') as f:
    json.dump(user_group, f)
with open('json/user_macro.json', 'w') as f:
    json.dump(user_macro, f)
with open('json/value_map.json', 'w') as f:
    json.dump(value_map, f)
with open('json/web_services.json', 'w') as f:
    json.dump(web_services, f)

pprint(f"Demorou: {time.time() - tempo_inicial}")