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

from eventlet import wsgi
from eventlet import GreenPool
from eventlet import listen
from eventlet.green import socket
import eventlet
"""
from oslo_config import cfg
from paste import deploy
import pecan
from werkzeug import serving

from ceilometer.api import config as api_config
from ceilometer.api import hooks
from ceilometer.api import middleware
from ceilometer.i18n import _
from ceilometer.i18n import _LW
from ceilometer.openstack.common import log
from ceilometer import service

LOG = log.getLogger(__name__)

CONF = cfg.CONF

OPTS = [
    cfg.StrOpt('api_paste_config',
               default="api_paste.ini",
               help="Configuration file for WSGI definition of API."
               ),
    cfg.IntOpt('api_workers', default=1,
               help='Number of workers for Ceilometer API server.'),
]

API_OPTS = [
    cfg.BoolOpt('pecan_debug',
                default=False,
                help='Toggle Pecan Debug Middleware.'),
]

CONF.register_opts(OPTS)
CONF.register_opts(API_OPTS, group='api')

"""
def setup_app(pecan_config=None, extra_hooks=None):
    #print 'setup_app pecan_config %s'%pecan_config
    app = pecan.make_app(
        pecan_config.app.root,
        debug=True,
        #force_canonical=getattr(pecan_config.app, 'force_canonical', True),
        #guess_content_type_from_ext=False
    )
    #print 'return setup_app'
    return app


def get_pecan_config():
    # Set up the pecan configuration
    filename = api_config.__file__.replace('.pyc', '.py')
    #filename = config.py
    #print 'pecan config %s'%filename
    return pecan.configuration.conf_from_file(filename)

class RestrictedGreenPool(GreenPool):
    """
    Works the same as GreenPool, but if the size is specified as one, then the
    spawn_n() method will invoke waitall() before returning to prevent the
    caller from doing any other work (like calling accept()).
    """
    def __init__(self, size=1024):
        super(RestrictedGreenPool, self).__init__(size=size)
        self._rgp_do_wait = (size == 1)

    def spawn_n(self, *args, **kwargs):
        super(RestrictedGreenPool, self).spawn_n(*args, **kwargs)
        if self._rgp_do_wait:
            self.waitall()

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
    #cfg_path = cfg.CONF.api_paste_config
    cfg_path = '/root/pecan_test/test_project/api_paste.ini'
    if not os.path.isabs(cfg_path):
        cfg_file = CONF.find_file(cfg_path)
    elif os.path.exists(cfg_path):
        cfg_file = cfg_path

    if not cfg_file:
        raise cfg.ConfigFilesNotFoundError([cfg.CONF.api_paste_config])
    #LOG.info("Full WSGI config used: %s" % cfg_file)
    print 'api paste file %s'%cfg_file
    return deploy.loadapp("config:" + cfg_file)


# you must apply body for post method such as curl -X POST 'http://localhost:8080/v2/query2' -d "dddd"

def build_server():
    print 'start to build paste server'


    eventlet.hubs.use_hub('poll')
    eventlet.patcher.monkey_patch(all=False, socket=True)


    app = load_app()
    # Create the WSGI server and start it
    #host, port = cfg.CONF.api.host, cfg.CONF.api.port
    host = '0.0.0.0'
    port = '8080'

    #LOG.info(_('Starting server in PID %s') % os.getpid())
    #LOG.info(_("Configuration:"))
    #cfg.CONF.log_opt_values(LOG, logging.INFO)

    if host == '0.0.0.0':
        #LOG.info(_(
        #    'serving on 0.0.0.0:%(sport)s, view at http://127.0.0.1:%(vport)s')
        #    % ({'sport': port, 'vport': port}))
        print 'port %s'%port
    else:
        #LOG.info(_("serving on http://%(host)s:%(port)s") % (
        #         {'host': host, 'port': port}))
        print 'host %s'%host

    #workers = service.get_workers('api')
    workers =1
    #serving.run_simple(host, port,
    #                  app, processes=workers, threaded=1)
    serving.run_simple(host, port,
                      app, processes=workers)
    """
    pool = RestrictedGreenPool(size=1024)
    print 'running pool %s'%pool
    serving.run_simple(host, port,
                       app, processes=pool)
    """


def app_factory(global_config, **local_conf):
    print 'into app_factory'
    return VersionSelectorApplication()

