import logging  
import logging.handlers
  
logger = logging.getLogger(__name__)  
logger.setLevel(logging.DEBUG)  
  
fh = logging.FileHandler('/var/log/test.log')  
fh.setLevel(logging.DEBUG)  
  
ch = logging.StreamHandler()  
ch.setLevel(logging.DEBUG)  
handler = logging.handlers.SysLogHandler(address = '/dev/log')
fh.addHandler(handler)
  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  
  
logger.addHandler(fh)  
logger.addHandler(ch)  
  
logger.info('foorbar')  
