

import time


class updatorServer(object):
    
    def __init__(self):
        self.all_components=['adminPortal','userPortal','fileop','notiserver','rabbitmq','mongodb']
        pass
    def _update_all(self):
        #clean folder
        #wget stuff from message, need more argv
        #untar
        #remove old folder 
        #goto every folder and install all
        time.sleep(10)
        return 'OK'
    def _update_software(self, service):
        print 'into update software', service
        result = service +'....'+'OK'
        if service =='all':
            self._update_all()
        return result


    def update_software(self, service):
        #for component in self.all_components:
        #    print 'update software %s ....',component
        #print 'update software :%s: done'%service
        ret = self._update_software(service)
        return ret

    def sync_software(self, service):
        return 'sync software done ....'


    def update_firmware(self, service):
        return 'sync software done ....'
    
