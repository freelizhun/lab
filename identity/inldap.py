#import ldap,ldif,sys
import ldap,sys
ld = ldap.initialize('ldap://mon0:389')
ld.simple_bind_s()
#basedn = "ou=users,dc=openstack,dc=org"
basedn = "dc=openstack,dc=org"
searchFilter = "cn=*"
results = ld.search_s(basedn,ldap.SCOPE_SUBTREE, searchFilter)
listuser=[]
for dn,entry in results:
    dn = str(dn)
    #print dn
    name = dn.split(',')[0].split('=')[1]
    print name
    if name not in listuser:
        listuser.append(name)
    
print listuser
