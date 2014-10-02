
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('multisection.ini')

print 'URL:', parser.get('bug_tracker', 'url')
