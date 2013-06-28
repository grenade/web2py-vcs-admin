# coding: utf8

import svn_admin
repo_list=svn_admin.get_repo_list()

def index():
    return dict(title='Repository Administration', repo_list=repo_list)

@auth.requires_login()
def config():
    if len(request.args) >= 2:
        config_dict=svn_admin.get_repo_config(request.args[0], request.args[1])
        if request.args[1] == 'authz' and 'groups' in config_dict and 'approvers' in config_dict['groups'] and auth.user.username in config_dict['groups']['approvers']:
            form = FORM(UL(LI('approvers (group admins):', BR(), INPUT(_name='approvers', _value=config_dict['groups']['approvers'], _style='width:100%', requires=IS_LENGTH(minsize=6))),
                        LI('contributors (read/write):', BR(), INPUT(_name='contributors', _value=config_dict['groups']['contributors'], _style='width:100%')),
                        LI('lurkers (read-only):', BR(), INPUT(_name='lurkers', _value=config_dict['groups']['lurkers'], _style='width:100%'), BR(),
                        INPUT(_type='submit', _value='update groups', _style='float:right'))))
            if form.accepts(request,session):
                svn_admin.set_groups(request.args[0], request.vars.approvers, request.vars.contributors, request.vars.lurkers)
                config_dict=svn_admin.get_repo_config(request.args[0], request.args[1])
                response.flash = 'groups updated!'
            elif form.errors:
                response.flash = 'groups not updated'
            else:
                return dict(title=request.args[0], config_dict=config_dict, form=form, repo_list=repo_list)
            pass
        pass
        return dict(title=request.args[0], config_dict=config_dict, repo_list=repo_list)
    else:
        return redirect(URL('index'))
    pass

@auth.requires_login()
def user():
    if len(request.args) == 1 and request.args[0] == 'password':
        form = FORM(DIV('new password:', BR(), INPUT(_name='svn_password_a', _type='password', requires=IS_LENGTH(minsize=6, maxsize=32))),
          DIV('confirm password:', BR(), INPUT(_name='svn_password_b', _type='password', requires=IS_EQUAL_TO(request.vars.svn_password_a, error_message='passwords do not match'))),
          DIV('svn repository:', BR(), SELECT(*(['all'] + repo_list), **dict(_name='repo'))),
          INPUT(_type='submit', _value='set password'))
        if form.accepts(request,session):
            svn_admin.set_password(request.vars.repo, auth.user.username, request.vars.svn_password_a)
            response.flash = 'well done! your password has been set.'
        elif form.errors:
            response.flash = 'bummer! your password has not yet been set.'
        else:
            response.flash = "you're smart! you've come to the right place to set your svn password."
        return dict(title=request.args[0], form=form, repo_list=repo_list)
    return redirect(URL('index'))
