# Sample Python module to use python plugin 

import collectd
import random

#== Our Own Functions go here: ==#
def configer(ObjConfiguration):
   collectd.debug('Configuring Stuff') 
   collectd.info('collectdinfo') 
   for node in ObjConfiguration.children:
       collectd.info('collectshow %s %s'%(node.key, node.values[0]))

def initer():
    collectd.debug('initing stuff')

def reader(input_data=None):
    metric = collectd.Values();
    metric.plugin = 'python_plugin_test'
    metric.type = 'gauge'
    metric.type_instance = 'gg'
    #metric.values = [100]
    metric.values = [random.random()*100]
    metric.host = 'lab-ser-kvm-172016000011_cloudcube_com_tw'
    metric.dispatch()

    metric1 = collectd.Values();
    metric1.host = 'lab-ser-kvm-172016000011_cloudcube_com_tw'
    metric1.plugin = 'python_plugin_test'
    metric1.type = 'gauge'
    metric1.type_instance = 'tt'
    #metric.values = [100]
    metric1.values = [random.random()*100]
    metric1.dispatch()

#== Hook Callbacks, Order is important! ==#
collectd.register_config(configer)
collectd.register_init(initer)
collectd.register_read(reader, 5)
