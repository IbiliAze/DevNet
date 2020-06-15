from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle("10.10.20.113", "ucspe", "ucspe")
handle.login()
org = handle.query_classid(class_id='orgOrg', hierarchy=True)

servers = handle.query_classid("ComputeBlade")

for server in servers:
    print(server.dn, server.available_memory)
    print(servers)

blade = handle.query_dn('sys/chasis-3/blade-1')
print(blade)

