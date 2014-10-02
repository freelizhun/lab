import logging
import logging.handlers



my_logger = logging.getLogger('monga-fcupgrade')
my_logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('/var/log/monga-fc.log')
fh.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address = '/dev/log')
formatter = logging.Formatter('%(name)s: %(levelname)s - %(message)s')
handler.setFormatter(formatter)
formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter1)
my_logger.addHandler(handler)
my_logger.addHandler(fh)
status = 1

a = 'hahaha'
my_logger.debug('this is debug %s'%a)
my_logger.debug('show status  %s'%status)
my_logger.info('this is info')
my_logger.info('this is info')


