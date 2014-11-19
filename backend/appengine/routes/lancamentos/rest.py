# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse
from lancamento_app import facade

@login_not_required
@no_csrf
def index():
    cmd = facade.list_lancamentos_cmd()
    lancamento_list = cmd()
    short_form=facade.lancamento_short_form()
    lancamento_short = [short_form.fill_with_model(m) for m in lancamento_list]
    return JsonResponse(lancamento_short)


def save(_resp, **lancamento_properties):
    cmd = facade.save_lancamento_cmd(**lancamento_properties)
    return _save_or_update_json_response(_resp, cmd)

@login_not_required
@no_csrf
def update(_resp, lancamento_id, **lancamento_properties):
    cmd = facade.update_lancamento_cmd(lancamento_id, **lancamento_properties)
    return _save_or_update_json_response(_resp, cmd)

@login_not_required
@no_csrf
def delete(lancamento_id):
    facade.delete_lancamento_cmd(lancamento_id)()


def _save_or_update_json_response(_resp,cmd):
    try:
        lancamento = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    short_form=facade.lancamento_short_form()
    return JsonResponse(short_form.fill_with_model(lancamento))

