

from oslo_config import cfg

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

cfg.CONF.register_opts(ALARM_API_OPTS, group='alarm')


class alm(object):
    def __init__(self):
        user_record_history = cfg.CONF.alarm.record_history
        print 'user record %s'%user_record_history
        print cfg.CONF.alarm.alarm_sec




        
