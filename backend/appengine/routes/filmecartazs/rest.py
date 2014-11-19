# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from filmecartaz_app import facade


def index():
    cmd = facade.list_cartazs_cmd()
    cartaz_list = cmd()
    short_form=facade.cartaz_short_form()
    cartaz_short = [short_form.fill_with_model(m) for m in cartaz_list]
    return JsonResponse(cartaz_short)


def save(_resp,**cartaz_properties):
    cmd = facade.save_cartaz_cmd(**cartaz_properties)
    return _save_or_update_json_response(_resp,cmd)


def update(_resp,cartaz_id, **cartaz_properties):
    cmd = facade.update_cartaz_cmd(cartaz_id, **cartaz_properties)
    return _save_or_update_json_response(_resp,cmd)


def delete(cartaz_id):
    facade.delete_cartaz_cmd(cartaz_id)()


def _save_or_update_json_response(_resp,cmd):
    try:
        cartaz = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    short_form=facade.cartaz_short_form()
    return JsonResponse(short_form.fill_with_model(cartaz))

