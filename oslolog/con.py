

from oslo_config import cfg
import common.oslolog as logging

ALARM_API_OPTS = [
    cfg.BoolOpt('record_history',
                default=False,
                help='Record alarm change events.'
                ),
    cfg.StrOpt('alarm_sec',
                default=0,
                help='Record alarm change events.'
                ),
]
CONF = cfg.CONF
CONF.register_opts(ALARM_API_OPTS, group='alarm')
LOG = logging.getLogger(__name__)

class alm(object):
    def __init__(self):
        user_record_history = CONF.alarm.record_history
        LOG.info('user record %s'%user_record_history)
        LOG.info(CONF.alarm.alarm_sec)




        
