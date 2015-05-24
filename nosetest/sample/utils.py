from testconfig import config

def showConfig(config):
    print config['global']['keystone_ip']
    print config['global']['controller_ip']
    print config['global']['user_name']
    print config['global']['password']

def getToken():
    print 'into get token'
    print config['global']['keystone_ip']
    print config['global']['controller_ip']
    print config['global']['user_name']
    print config['global']['password']
    return 'haha'
    
