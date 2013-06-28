#!/usr/bin/env python
# coding: utf8
from gluon import *
from ConfigParser import SafeConfigParser
import os

svn_dir = '/data/svn'

def get_repo_list():
    return os.listdir(svn_dir)

def get_repo_config(repo, config):
    parser = SafeConfigParser()
    parser.read(os.path.join(svn_dir, repo, 'conf', config))
    return {section:{option:parser.get(section,option) for option in parser.options(section)} for section in parser.sections()}

def set_password(repo, username, password):
    if repo == 'all':
        for repo_name in get_repo_list():
            set_password(repo_name, username, password)
    else:
        config_file = os.path.join(svn_dir, repo, 'conf', 'passwd')
        parser = SafeConfigParser()
        parser.read(config_file)
        parser.set('users', username, password)
        parser.write(open(config_file, 'w'))
    return

def set_groups(repo, approvers, contributors, lurkers):
    config_file = os.path.join(svn_dir, repo, 'conf', 'authz')
    parser = SafeConfigParser()
    parser.read(config_file)
    parser.set('groups', 'approvers', approvers)
    parser.set('groups', 'contributors', contributors)
    parser.set('groups', 'lurkers', lurkers)
    parser.write(open(config_file, 'w'))
    return
