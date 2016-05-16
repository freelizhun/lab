#
# Copyright 2012 New Dream Network, LLC (DreamHost)
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging
import os
import pecan
from paste import deploy
import config as api_config
from werkzeug import serving
import hooks
from paste.translogger import TransLogger
from oslo_config import cfg
import sys

#CONF = cfg.CONF(default_config_files=['app.conf'])
CONF = cfg.CONF
OPTS = [
    cfg.StrOpt('api_paste_config',
               default="api_paste.ini",
               help="Configuration file for WSGI definition of API."
               ),
    cfg.IntOpt('api_workers', default=1,
               help='Number of workers for Ceilometer API server.'),
    cfg.StrOpt('host',
               default='0.0.0.0',
               help='The listen IP for the ceilometer API server.',
               ),
    cfg.IntOpt('port',
               default=8777,
               deprecated_name='metering_api_port',
               deprecated_group='DEFAULT',
               help='The port for the ceilometer API server.',
               ),
    cfg.IntOpt('workers', default=1,
               help='Number of workers for Ceilometer API server.'),
    cfg.IntOpt('threaded', default=100,
               help='Number of threaded for Ceilometer API server.'),
]

API_OPTS = [
    cfg.BoolOpt('pecan_debug',
                default=False,
                help='Toggle Pecan Debug Middleware.'),
]

CONF.register_opts(OPTS)
CONF.register_opts(OPTS, group='api')



def setup_app(pecan_config=None, extra_hooks=None):
    #print 'setup_app pecan_config %s'%pecan_config
    app_hooks = [hooks.ConfigHook(),
                 hooks.SecondHook(),
                ]


    app = pecan.make_app(
        pecan_config.app.root,
        debug=True,
        hooks=app_hooks,
        #force_canonical=getattr(pecan_config.app, 'force_canonical', True),
        #guess_content_type_from_ext=False
    )
    app = TransLogger(app, setup_console_handler=False)

    #print 'return setup_app'
    return app


def get_pecan_config():
    # Set up the pecan configuration
    filename = api_config.__file__.replace('.pyc', '.py')
    #filename = config.py
    #print 'pecan config %s'%filename
    return pecan.configuration.conf_from_file(filename)


class VersionSelectorApplication(object):
    def __init__(self):
        pc = get_pecan_config()
        self.v2 = setup_app(pecan_config=pc)
        #self.v2 = setup_app()

    def __call__(self, environ, start_response):
        if environ['PATH_INFO'].startswith('/v1/'):
            return self.v1(environ, start_response)
        #print 'into v2'
        return self.v2(environ, start_response)


def load_app():
    # Build the WSGI app
    cfg_file = None
    cfg_path = cfg.CONF.api_paste_config
    if not os.path.isabs(cfg_path):
        print 'show config path ----- %s'%cfg_path
        cfg_file = CONF.find_file(cfg_path)
    elif os.path.exists(cfg_path):
        cfg_file = cfg_path
        print 'show config file-------%s'%cfg_file

    if not cfg_file:
        raise cfg.ConfigFilesNotFoundError([cfg.CONF.api_paste_config])
    print '-------------------api paste file %s'%cfg_file
    return deploy.loadapp("config:" + cfg_file)


# you must apply body for post method such as curl -X POST 'http://localhost:8080/v2/query2' -d "dddd"

def build_server():
    print 'start to build paste server'
    

    print 'sysarg %s'%sys.argv[1:]
    app = load_app()

    #host = cfg.CONF.api.host
    #port = cfg.CONF.api.port
    host = CONF.api.host
    port = CONF.api.port
    print 'the configuration parameters %s %s'%(host, port)


    #workers = service.get_workers('api')
    workers=CONF.api.workers
    threaded=CONF.api.threaded
    serving.run_simple(host, port,
                      app, processes=workers, threaded=threaded)
    #serving.run_simple(host, port,
    #                  app, processes=workers)


def app_factory(global_config, **local_conf):
    print 'into app_factory'
    return VersionSelectorApplication()

