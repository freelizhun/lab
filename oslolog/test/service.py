import sys
from oslo_config import cfg
import oslolog as logging

def prepare_service(argv=None):
    CONF = cfg.CONF(sys.argv[1:], project='ceilometer', validate_default_values=True)
    DOMAIN = "ceilometer"
    logging.setup(CONF, DOMAIN)
    #logging.setup("app")
