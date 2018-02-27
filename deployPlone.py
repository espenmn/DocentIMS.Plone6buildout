#!/usr/bin/python

import os
from os.path import expanduser
import sys

try:
    import sh
except ImportError, e:
    print "Please install the 'sh' python package in your system python with the following command: easy_install-2.7 sh"
    sys.exit(-1)
print "Found sh"

try:
    import virtualenv
except ImportError, e:
    print "Please install the 'virtualenv' python package in your system python with the following command: easy_install-2.7 virtualenv"
    sys.exit(-1)
print "Found virtualenv"

"""
paths are based on the current working directory assumed to be the instance home
script will create a python virtual env, buildout caches and run buildout
"""

PATH_TO_INSTANCE_HOME = os.getcwd()
INSTANCE_HOME_DIRNAME = os.path.split(PATH_TO_INSTANCE_HOME)[1]

PATH_TO_USER_HOME = expanduser("~")
PATH_TO_PLONE_ASSETS = '%s/plone' % PATH_TO_USER_HOME
PATH_TO_BACKUPS = '%s/backups' % PATH_TO_PLONE_ASSETS
PATH_TO_INSTANCE_BACKUP = '%s/%s' % (PATH_TO_BACKUPS, INSTANCE_HOME_DIRNAME)
PATH_TO_VIRTUAL_ENV = '%s/python27' % PATH_TO_PLONE_ASSETS
PATH_TO_BUILDOUT_CACHE = '%s/buildout-cache' % PATH_TO_PLONE_ASSETS
PATH_TO_CACHE_EGGS = '%s/eggs' % PATH_TO_BUILDOUT_CACHE
PATH_TO_DOWNLOADS = '%s/downloads' % PATH_TO_BUILDOUT_CACHE
PATH_TO_CMMI = '%s/cmmi' % PATH_TO_DOWNLOADS
PATH_TO_DIST = '%s/dist' % PATH_TO_DOWNLOADS
PATH_TO_CHECKOUTS = '%s/checkouts' % PATH_TO_PLONE_ASSETS

#setup plone assets
os.chdir(PATH_TO_USER_HOME)
if not os.path.exists(PATH_TO_PLONE_ASSETS):
	print "Creating Plone Asset Directory"
	os.mkdir(PATH_TO_PLONE_ASSETS)

if not os.path.exists(PATH_TO_CHECKOUTS):
	print "Creating Checkouts Directory"
	os.mkdir(PATH_TO_CHECKOUTS)

if not os.path.exists(PATH_TO_BUILDOUT_CACHE):
	print "Creating Buildout Cache"
	os.mkdir(PATH_TO_BUILDOUT_CACHE)

if not os.path.exists(PATH_TO_CACHE_EGGS):
	print "Creating Eggs Cache"
	os.mkdir(PATH_TO_CACHE_EGGS)

if not os.path.exists(PATH_TO_DOWNLOADS):
	print "Creating Downloads Cache"
	os.mkdir(PATH_TO_DOWNLOADS)

if not os.path.exists(PATH_TO_CMMI):
	print "Creating CMMI Cache"
	os.mkdir(PATH_TO_CMMI)

if not os.path.exists(PATH_TO_DIST):
	print "Creating DIST Cache"
	os.mkdir(PATH_TO_DIST)

if not os.path.exists(PATH_TO_BACKUPS):
	print "Creating BACKUPS Directory"
	os.mkdir(PATH_TO_BACKUPS)

if not os.path.exists(PATH_TO_INSTANCE_BACKUP):
	print "Creating Instance Backup Directory"
	os.mkdir(PATH_TO_INSTANCE_BACKUP)

if not os.path.exists(PATH_TO_VIRTUAL_ENV):
	#setup virtualenv
	print "Creating Virtual Env"
	sys_virtual_env = sh.virtualenv
	sys_python_path = sh.which('python2.7')
	sys_virtual_env('--no-site-packages', '--python=%s' % sys_python_path, PATH_TO_VIRTUAL_ENV)


print "Bootstrapping Instance"
os.chdir(PATH_TO_INSTANCE_HOME)

if not os.path.exists('./src'):
    os.symlink(PATH_TO_CHECKOUTS, './src')

wget = sh.Command(sh.which('wget'))
wget('-O', 'bootstrap.py', 'https://bootstrap.pypa.io/bootstrap-buildout.py')
print "Got bootstrap.py"

p5_python = sh.Command('%s/bin/python2.7' % PATH_TO_VIRTUAL_ENV)
p5_python('./bootstrap.py', '-c', './buildout_master.cfg')

print "%s ready to run buildout. Make sure to update buidout_master with proper admin credentials FIRST." \
      " You must also update the path to backup files: %s. If this is your first time running buildout on" \
      " this system it may take a while." % (INSTANCE_HOME_DIRNAME, PATH_TO_INSTANCE_BACKUP)
