from six.moves.urllib import parse
from httplib2 import Http
import json
admin_token='90872f53cf534bf98292693ffe31c1ac'

def build_url(path, q, params=None):
    '''This converts from a list of dicts and a list of params to
       what the rest api needs, so from:
    "[{field=this,op=le,value=34},{field=that,op=eq,value=foo}],
     ['foo=bar','sna=fu']"
    to:
    "?q.field=this&q.op=le&q.value=34&
      q.field=that&q.op=eq&q.value=foo&
      foo=bar&sna=fu"
    '''
    if q:
        query_params = {'q.field': [],
                        'q.value': [],
                        'q.op': [],
                        'q.type': []}

        for query in q:
            for name in ['field', 'op', 'value', 'type']:
                query_params['q.%s' % name].append(query.get(name, ''))

        # Transform the dict to a sequence of two-element tuples in fixed
        # order, then the encoded string will be consistent in Python 2&3.
        new_qparams = sorted(query_params.items(), key=lambda x: x[0])
        path += "?" + parse.urlencode(new_qparams, doseq=True)

        if params:
            for p in params:
                path += '&%s' % p
    elif params:
        path += '?%s' % params[0]
        for p in params[1:]:
            path += '&%s' % p
    return path

def build_path(meter_name, meter_type='statistics'):
    #path ='http://localhost:8777/v2/meters/cpu_util/statistics'
    path ='http://localhost:8777/v2/meters/%s/%s'%(meter_name, meter_type)
    return path

def get_metaname_stat(meta_name, project_id):
    #path = build_path('cpu_util')
    path = build_path(meta_name)
    q=[{"field":"timestamp","op":"ge","value":"2014-09-29T13:34:17","type":"None"},
    {'field':'project_id','op':'eq','value':project_id}]
    full_path= build_url(path,q)

    h = Http()
    headers = {'Content-type': 'application/json','X-Auth-Token':'%s'%admin_token}
    esp, content = h.request("%s"%full_path, headers=headers)
    datas = json.loads(content)

    for data in datas:
        print '%s usage %s for this tenant %s'%(meta_name, data['sum'],project_id)


project_id='5bee4ac21f2844439b76665ba65ee952'
get_metaname_stat('cpu_util', project_id)
get_metaname_stat('disk.write.bytes', project_id)
get_metaname_stat('disk.read.bytes', project_id)
get_metaname_stat('network.incoming.bytes', project_id)
get_metaname_stat('network.outgoing.bytes', project_id)

