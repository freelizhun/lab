import ceilometerclient.v2 as c_client
import keystoneclient.v2_0.client as k_client
#from constants import *

OS_USERNAME="admin"
OS_PASSWORD="1234"
OS_TENANT_NAME="admin"
OS_AUTH_URL="http://10.90.0.89:5000/v2.0/"
CEILOMETER_ENDPOINT="http://10.90.0.89:8777"

keystone = k_client.Client(auth_url=OS_AUTH_URL, username=OS_USERNAME,password=OS_PASSWORD, tenant_name=OS_TENANT_NAME)
print keystone.auth_token
auth_token = keystone.auth_token
print auth_token
ceilometer = c_client.Client(endpoint=CEILOMETER_ENDPOINT, token= lambda : auth_token )
meterlist = ceilometer.meters.list()
print meterlist
cpu_util_sample = ceilometer.samples.list('cpu_util')

#for each in cpu_util_sample:
#    print each.timestamp, each.resource_id, each.counter_volume
