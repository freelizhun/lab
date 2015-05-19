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
from otherclass import OtherWorker

SLEEP_BETWEEN_AUDITS = 30


class StoreWorker(object):
    """Walk through file system to audit objects"""

    def __init__(self, conf, logger):
        self.conf = conf
        self.logger = logger


    def audit_all_objects(self):
        print "test"
        print '%s'%self.conf
        self.logger.info('into main job')



class DataStore(Daemon):
    """Audit objects."""

    def __init__(self, conf, logger, **options):
        self.conf = conf
        #self.logger = get_logger(conf, log_route='object-auditor')
        self.logger = logger

    def _sleep(self):
        time.sleep(SLEEP_BETWEEN_AUDITS)


    def run_store(self, **kwargs):
        """Run the object audit"""
        worker = StoreWorker(self.conf, self.logger)
        worker.audit_all_objects()
        worker2 = OtherWorker(self.conf, self.logger)
        worker2.other_all_objects()


    def store_loop(self, **kwargs):
        """Parallel audit loop"""
        print (("check conf %s")%self.conf)
        self.run_store(**kwargs)

    def run_forever(self, *args, **kwargs):
        """Run the object audit until stopped."""
        # zero byte only command line option
        print 'run_forever'
        self.logger.info("test check logger")
        self.store_loop(**kwargs)
        self._sleep()

    def run_once(self, *args, **kwargs):
        """Run the object audit once"""
        # zero byte only command line option
        self.store_loop(**kwargs)
