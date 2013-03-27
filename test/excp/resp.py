from webob.exc import *
import json

"""
Successful Messages
"""
def ok(content=None):
    return HTTPOk(app_iter = content,
        content_type='application/json')

def created():
    return HTTPCreated()

def no_content():
    return HTTPNoContent()

"""
Fail Messages
"""
def bad_request(error):
    return HTTPBadRequest(
        app_iter = gen_body(content = error),
        content_type = 'application/json')
        
def forbidden(error):
    return HTTPForbidden(
        app_iter = gen_body(content = error),
        content_type = 'application/json')

def service_unavaliable(error):
    return HTTPServiceUnavailable(
        app_iter = gen_body(content = error),
        content_type = 'application/json')

def internal_error(error):
    return HTTPInternalServerError(
        app_iter = gen_body(content = error),
        content_type = 'application/json')
def not_found(error):
    return HTTPNotFound(
        app_iter = gen_body(content = error),
        content_type = 'application/json')

def unauthorized(error):
    return HTTPUnauthorized(
        app_iter = gen_body(content = error),
        content_type = 'application/json')


"""
Send Fail Result
"""
def gen_body(content='', serv_name='monga'):
    data={}
    data['service']=serv_name
    data['details']=str(content)
    result={}
    result['fault']=data

    return [json.dumps(result,sort_keys=True,indent=4)]
