from acitoolkit.acitoolkit import *

url = 'https://sandboxapicdc.cisco.com'
user = 'admin'
pw = 'ciscopsdt'

session = Session(url, user, pw)
session.login()

tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)
    print(tenant.descr)
    print()

#Create a new Tenant   
new_tenant = Tenant("Tenant_Name_Here")

#Create a new APP Profile and a EPG. epg > anp > new_tenant (ROOT)
anp = AppProfile('Logi_APP', new_tenant)
epg = EPG('Logi_EPG', anp)

#Create a new context and a VLAN.
context = Context(Logi_VRF, new_tenant)
bridge_domain = BridgeDomain('Logi_Domain', new_tenant)

#bridge_domain > context > epg > anp > new_tenant
bridge_domain.add_context(context)
epg.add_bd(bridge_domain)
