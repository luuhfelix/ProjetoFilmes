# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from lancamento_app import facade
from routes.lancamentos import admin


@no_csrf
def index(lancamento_id):
    lancamento = facade.get_lancamento_cmd(lancamento_id)()
    detail_form = facade.lancamento_detail_form()
    context = {'save_path': router.to_path(save, lancamento_id), 'lancamento': detail_form.fill_with_model(lancamento)}
    return TemplateResponse(context, 'lancamentos/admin/form.html')


def save(_handler, lancamento_id, **lancamento_properties):
    cmd = facade.update_lancamento_cmd(lancamento_id, **lancamento_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'lancamento': cmd.form}

        return TemplateResponse(context, 'lancamentos/admin/form.html')
    _handler.redirect(router.to_path(admin))

