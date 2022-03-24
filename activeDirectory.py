import ldap3
from ldap3 import Server, Connection
from ldap3 import Server, Connection, SAFE_SYNC

from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as addUsersInGroups
server = Server('192.168.0.205')
conn = Connection(server, user ='glpi2', password ='glpiFtdw7', client_strategy=ldap3.SAFE_SYNC, auto_bind=True)

print(conn)
conn.search('DC=RZNPRO,DC=Local','(&(objectclass=user)(sAMAccountName=glpi2))')
# status, result, response, _ = conn.search('o=glpi2', '(objectclass=*)')  # usually you don't need the original request (4th element of the returned tuple)
# ldaps://172.16.10.50:636 - ssl - user: CN=ldap_bind_account,OU=1_Service_Accounts,OU=0_Users,DC=TG,DC=LOCAL - not lazy - bound - open - <local: 192.168.1.12:54408 - remote: 172.16.10.50:636> - tls not started - listening - SyncStrategy - internal decoder