# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse
from filme_app import facade

@login_not_required
@no_csrf
def index():
    cmd = facade.list_filmess_cmd()
    filmes_list = cmd()
    short_form=facade.filmes_short_form()
    filmes_short = [short_form.fill_with_model(m) for m in filmes_list]
    return JsonResponse(filmes_short)

@login_not_required
@no_csrf
def save(_resp,**filmes_properties):
    cmd = facade.save_filmes_cmd(**filmes_properties)
    return _save_or_update_json_response(_resp,cmd)

@login_not_required
@no_csrf
def update(_resp,filmes_id, **filmes_properties):
    cmd = facade.update_filmes_cmd(filmes_id, **filmes_properties)
    return _save_or_update_json_response(_resp,cmd)

@login_not_required
@no_csrf
def delete(filmes_id):
    facade.delete_filmes_cmd(filmes_id)()


def _save_or_update_json_response(_resp,cmd):
    try:
        filmes = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    short_form=facade.filmes_short_form()
    return JsonResponse(short_form.fill_with_model(filmes))

