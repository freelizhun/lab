# Server Specific Configurations
server = {
    'port': '8080',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'test_project.controllers.root.RootController',
    'modules': ['test_project'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/test_project/templates',
    'debug': True,
    'errors': {
        404: '/error/404',
        '__force_dict__': True
    }
}


logging = {
    'loggers': {
        # ...
        'wsgi': {'level': 'INFO', 'handlers': ['logfile'], 'qualname': 'wsgi'}
    },
    'handlers': {
        # ...
        'logfile': {
            'class': 'logging.FileHandler',
            'filename': '/var/log/tester.log',
            'level': 'INFO',
            'formatter': 'messageonly'
        }
    },
    'formatters': {
        # ...
        'messageonly': {'format': '%(message)s'}
    }
}

# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}
#
# All configurations are accessible at::
# pecan.conf
