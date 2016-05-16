#! /usr/bin/env python
from oslo.config import cfg
import sys
import con 
import service
from common import oslolog as logging
from common.i18n import _


LOG = logging.getLogger(__name__)

opt_simple_group = cfg.OptGroup(name='simple',
                         title='A Simple Example')
 
opt_moredata_group = cfg.OptGroup(name='moredata',
                         title='A More Complex Example')
simple_opts = [
    cfg.BoolOpt('enable', default=False,
                help=('True enables, False disables'))
]

moredata_opts = [
    cfg.StrOpt('message', default='No data',
               help=('A message')),
    cfg.ListOpt('usernames', default=None,
                help=('A list of usernames')),
    cfg.DictOpt('jobtitles', default=None,
                help=('A dictionary of usernames and job titles')),
    cfg.IntOpt('payday', default=30,
                help=('Default payday monthly date')),
    cfg.FloatOpt('pi', default=0.0,
                help=('The value of Pi'))
]


CONF = cfg.CONF
CONF.register_group(opt_simple_group)
CONF.register_opts(simple_opts, opt_simple_group)
 
CONF.register_group(opt_moredata_group)
CONF.register_opts(moredata_opts, opt_moredata_group)
 
 
if __name__ == "__main__":
    #CONF(sys.argv[1:], project='app')
    service.prepare_service()
    LOG.error(CONF.simple.enable)
    LOG.error(CONF.moredata.usernames)
    con.alm()
