from oslo_config import cfg
#from oslo_log import log as logging
from common import oslolog as logging
from common.i18n import _
import sys
import service
import runlog2 as r2


service.prepare_service()
LOG = logging.getLogger(__name__)

# Oslo Logging uses INFO as default
LOG.info("Oslo Logging")
LOG.warning("Oslo Logging")
LOG.error("Oslo Logging")


print 'start to log'

LOG.info("Oslo Logging")
namespace="haha"
LOG.error(_('loading notification handlers from %s'), namespace)
LOG.error(_('logtocomapre'))
r2.alarm()
