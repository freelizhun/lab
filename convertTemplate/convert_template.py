#!/usr/bin/env python
import os
import json
import shutil
from jinja2 import Environment, FileSystemLoader

software_package=os.path.dirname(os.path.realpath(__file__))+'/'
print software_package
#import time
#time.sleep(10)
if __name__=="__main__":
    # Set extension name list to filter "*.template"
    #ext_list = ['template','conf']
    ext_list = 'template'
    #ext_list = ''
    # Service configuration
    service_param_file =  software_package +'service_param.json'
    # Directory of the templates
    temp_dir = software_package+'template/'
    conf_dir = software_package+'config'
    #conf_dir = temp_dir
    try:
        shutil.copytree(temp_dir, conf_dir)
    except OSError:
        shutil.rmtree(conf_dir)
        shutil.copytree(temp_dir, conf_dir)
    with open(service_param_file) as param_file:    
        service_param = json.load(param_file)
    
    env = Environment(loader=FileSystemLoader(conf_dir))
    
    for temp in env.list_templates(ext_list):
        print '------------------------------'
        print 'Find template: ' + temp
        conf_content = env.get_template(temp).render(service_param)
        
        # Save the results
        conf_name, ext_name = os.path.splitext(conf_dir + temp)
        print 'temp', temp
        print 'Ext Name',ext_name
        print 'Save to ' + conf_name
        #with open(conf_dir+'/'+conf_name., "wb") as fh:
        writedir = conf_dir+'/'+temp.replace(ext_name,'')
        print writedir
        folder = writedir.rsplit('/',1)[0]
        print 'the folder:',folder
        if not os.path.exists(folder):  
            os.makedirs(folder)  
        with open(writedir , "w+") as fh:
            fh.write(conf_content)
            fh.close()
        
        os.remove(conf_dir+'/'+temp) 

