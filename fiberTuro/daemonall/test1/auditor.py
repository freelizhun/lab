# Copyright (c) 2010-2012 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import time
import signal
from random import shuffle
#from swift import gettext_ as _
from contextlib import closing
#from eventlet import Timeout
from utils import get_logger
#from swift.obj import diskfile
#from swift.common.utils import get_logger, ratelimit_sleep, dump_recon_cache, \
#    list_from_csv, json, listdir
#from swift.common.exceptions import DiskFileQuarantined, DiskFileNotExist
from daemon import Daemon

SLEEP_BETWEEN_AUDITS = 30


class AuditorWorker(object):
    """Walk through file system to audit objects"""

    def __init__(self):
        self.conf = []


    def audit_all_objects(self):
        print "test"



class ObjectAuditor(Daemon):
    """Audit objects."""

    def __init__(self, conf, logger, **options):
        self.conf = conf
        #self.logger = get_logger(conf, log_route='object-auditor')
        self.logger = logger
        print 'start to loginininini'
        self.logger.info('test')

    def _sleep(self):
        time.sleep(SLEEP_BETWEEN_AUDITS)


    def run_audit(self, **kwargs):
        """Run the object audit"""
        worker = AuditorWorker()
        worker.audit_all_objects()

    def fork_child(self, zero_byte_fps=False, **kwargs):
        """Child execution"""
        pid = os.fork()
        if pid:
            return pid
        else:
            signal.signal(signal.SIGTERM, signal.SIG_DFL)
            if zero_byte_fps:
                kwargs['zero_byte_fps'] = self.conf_zero_byte_fps
            try:
                self.run_audit(**kwargs)
            except Exception as e:
                self.logger.error(_("ERROR: Unable to run auditing: %s") % e)
            finally:
                sys.exit()

    def audit_loop(self, parent, zbo_fps, override_devices=None, **kwargs):
        """Parallel audit loop"""
        print (("check conf %s")%self.conf)
        self.run_audit(**kwargs)

    def run_forever(self, *args, **kwargs):
        """Run the object audit until stopped."""
        # zero byte only command line option
        print 'run_forever'
        self.logger.info("test check logger")
        zbo_fps = kwargs.get('zero_byte_fps', 0)
        parent = False
        if zbo_fps:
            # only start parent
            parent = True
        kwargs = {'mode': 'forever'}

        self.audit_loop(parent, zbo_fps, **kwargs)
        self._sleep()

    def run_once(self, *args, **kwargs):
        """Run the object audit once"""
        # zero byte only command line option
        self.audit_loop(parent, zbo_fps, override_devices=override_devices,
                        **kwargs)
