import ceilometerclient.v2 as c_client
import keystoneclient.v2_0.client as k_client
#from constants import *

OS_USERNAME="demo"
OS_PASSWORD="1234"
OS_TENANT_NAME="demo"
OS_AUTH_URL="http://10.90.0.89:5000/v2.0/"
CEILOMETER_ENDPOINT="http://10.90.0.89:8777"

keystone = k_client.Client(auth_url=OS_AUTH_URL, username=OS_USERNAME,password=OS_PASSWORD, tenant_name=OS_TENANT_NAME)
print keystone.auth_token
auth_token = keystone.auth_token
print auth_token
ceilometer = c_client.Client(endpoint=CEILOMETER_ENDPOINT, token= lambda : auth_token )
#period = []
#query.append({"field":"resource_id", "op": "eq", "value": "fb7e0e84-ea1e-4071-959d-307cbdfee6f1"})
period=[]
period.append({"field": "timestamp","op": "gt","value": "2003-06-01T00:00:00"})
meterlist = ceilometer.statistics.list(meter_name='cpu',  period= period)
print meterlist
meterlist = ceilometer.statistics.list(meter_name='cpu')
print meterlist
#print meterlist
#cpu_util_sample = ceilometer.samples.list('cpu_util')
#cpu_util_sample = ceilometer.list('cpu_util')

#for each in meterlist:
#    print each.timestamp, each.resource_id, each.counter_volume
