import time


def _getModifyTime():
    return time.strftime("%a, %d %b %Y %H:%M:%S %z")

def _getPath(req):
    return req.environ.get('HTTP_FILEPATH')

def _getMimeType(req):
    return req.environ.get('CONTENT_TYPE')

def upload(size, req):
    ret = {}
    ret['size']=str(int(size)/1024)+'KB'
    ret['thumb_exists']='false'
    ret['bytes']=size
    ret['modified']=_getModifyTime()
    ret['path']=_getPath(req)
    ret['id_dir']='false'
    ret['icon']='None'
    ret['root']='Tennant Name' 
    ret['mime_type']=_getMimeType(req)
    ret['revision']='None'
    return ret

def download(size, req):
    ret = {}
    ret['size']=str(int(size)/1024)+'KB'
    ret['thumb_exists']='false'
    ret['bytes']=size
    ret['modified']=_getModifyTime()
    ret['path']=_getPath(req)
    ret['id_dir']='false'
    ret['icon']='None'
    ret['root']='Tennant Name' 
    ret['mime_type']=_getMimeType(req)
    ret['revision']='None'
    return ret
