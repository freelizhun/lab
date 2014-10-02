import os
import random
#all file from tar.gz
#all tar.gz in same directory 
#checking tar.gz in directory 
#to deb
#get pip-requres's dep and tar to same directory
#finished job should be killed .tar.gz for next checking

import os
import sys
software_package='./packages'
deb_packages='/root/packages'
done_list=[]
def setupInit():
    #if sys.argv[1]=='clean':
    linuxCommand('rm -rf %s/*'%deb_packages)
    pass
def getallpackage(path):
    listtarfile = []
    for files in os.listdir("%s"%path):
        if files.endswith(".tar.gz") or files.endswith('zip'):
            listtarfile.append(files)
            #print files
    if not listtarfile:
        return False
    return listtarfile
def randomSelect(listtarfiles):
    return random.choice(listtarfiles)       
def linuxCommand(cmd):
    os.system(cmd)

def createDeb(targetfile):


    currentdir = os.getcwd()
    os.chdir('%s'%software_package)

    if targetfile in done_list:
        linuxCommand('rm -rf %s'%targetfile)
        os.chdir(currentdir)
        return 
        
    if targetfile.endswith('.zip'):
        targetDir = targetfile.split('.zip')[0]
    else:
        targetDir = targetfile.split('.tar.gz')[0]

    
    if targetfile.endswith('.zip'):
        linuxCommand('unzip %s'%targetfile)
    else:
        linuxCommand('tar zxvf %s'%targetfile)
    #download all dep 
    if targetDir == 'swift-master':
        untargetDir = 'swift-1.9.0'
    else:
        untargetDir = targetDir
    linuxCommand('mkdir dep')
    linuxCommand('mkdir dep1')
    linuxCommand('mkdir dep2')
    
    if os.path.isfile('%s/tools/pip-requires'%untargetDir):
        linuxCommand('pip install --download ./dep -r %s/tools/pip-requires'%untargetDir)
    if os.path.isfile('%s/tools/test-requires'%untargetDir):
        linuxCommand('pip install --download ./dep1 -r %s/tools/test-requires'%untargetDir)
    eggdir = targetfile.split('-')[0]+'.egg-info'
    if os.path.isfile('%s/%s/requires.txt'%(untargetDir,eggdir)):
        linuxCommand('pip install --download ./dep2 -r %s/%s/requires.txt'%(untargetDir,eggdir))
    
    linuxCommand('mv dep/* %s/%s'%(currentdir,software_package))
    linuxCommand('mv dep1/* %s/%s'%(currentdir,software_package))
    linuxCommand('mv dep2/* %s/%s'%(currentdir,software_package))

    os.chdir('%s'%untargetDir)
    linuxCommand('python setup.py --command-package=stdeb.command bdist_deb')
    linuxCommand('mv deb_dist/*.deb %s/.'%deb_packages)
    os.chdir('../')
    print targetDir
    if targetfile.endswith('.zip'):
        linuxCommand('rm -rf %s'%targetfile)
        linuxCommand('rm -rf %s'%untargetDir)
    else:
        linuxCommand('rm -rf %s'%targetfile)
        linuxCommand('rm -rf %s'%untargetDir)
    #linuxCommand('pip install --download ../ 
    #    -r %s/tools/test-requires'%targetDir)

    #build packages
    #os.system('cd %s'%targetdir)
    
    
    done_list.append(targetfile) 
    os.chdir(currentdir)

setupInit()
fileFlag = True
while fileFlag is True:
    print '----- get file list '
    listtarfiles = getallpackage('%s'%software_package)
    print '----- get file done '
    if not listtarfiles:
        break
    print '----- randomselect '
    targetfile = randomSelect(listtarfiles)
    print '----- the target file %s'%targetfile
    createDeb(targetfile)
    print '----- the target file done %s'%targetfile





