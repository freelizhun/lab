from webob import Request, Response
from routes import Mapper

url_mapper = Mapper()

def dispatch_app(environ, start_response):
    """Simplest possible application object"""
    request = Request(environ)
    __import__('urls')                 # load url configs
    matcher = url_mapper.match(request.path_info)
    callback = string_import(matcher['views'])
    response = Response(body=callback(request) , content_type='text/plain')
    return response(environ, start_response)

def string_import(module_path):
    path, _sep, name = module_path.rpartition('.')
    module = __import__(path, globals(), locals(), -1)
    return getattr(module, name)
