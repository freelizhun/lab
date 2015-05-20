class OtherWorker(object):
    """Walk through file system to audit objects"""

    def __init__(self, conf, logger):
        self.conf = conf
        self.logger = logger


    def other_all_objects(self):
        print "test"
        print '%s'%self.conf
        self.logger.info('into other main job')

