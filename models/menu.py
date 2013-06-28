# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Dev',SPAN('Ops')), _class="brand", _href=URL('devops', 'default', 'index'))
response.title = request.controller #request.application.replace('_',' ').title()
response.subtitle = T('repository administration')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Rob Thijssen <robin.thijssen@maersk.com>'
response.meta.description = 'yet another subversion repository administration interface'
response.meta.keywords = 'subversion, svn, repository administration'
response.meta.generator = 'subversion repository administration'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    #response.menu += [
    response.menu = [
        (T('source control'), False, URL('devops', 'default', 'index/vcs'), [
          (T('svn'), False, URL('vcs', 'svn', 'index'), [
            (T('rcm'), False, URL('vcs', 'svn', 'index/rcm')),
            (T('soa'), False, URL('vcs', 'svn', 'index/soa')),
            (T('utm'), False, URL('vcs', 'svn', 'index/utm'))]),
          ('git', False, URL('vcs', 'git', 'index'), [
            (T('repo-a'), False, URL('vcs', 'git', 'index/repo-a')),
            (T('repo-b'), False, URL('vcs', 'git', 'index/repo-b')),
            (T('repo-c'), False, URL('vcs', 'git', 'index/repo-c'))])])]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
