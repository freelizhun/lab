

import oslolog as logging
import service
from oslo_config import cfg
import sys


CONF = cfg.CONF
LOG = logging.getLogger(__name__)

print 'into test2'
#it will not show in file

LOG.error("Oslo logging in test2------------")

class alarm(object):
    def __init__(self):
        #it will show in file
        LOG.error("Oslo logging in test2's alarm------------")

