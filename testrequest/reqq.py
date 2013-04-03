from webob import Request


req = Request.blank('/a/c', headers={'': ''})
print req.environ
print req
