
from oslo_config import cfg
import sys
import common.oslolog as logging

def prepare_service(argv=None):
    if argv is None:
        argv = sys.argv
    cfg.CONF(argv[1:], project='app', validate_default_values=True)
    CONF=cfg.CONF
    DOMAIN = "app"
    logging.setup(CONF, DOMAIN)
