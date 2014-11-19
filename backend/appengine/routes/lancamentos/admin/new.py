# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from lancamento_app import facade
from routes.lancamentos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'lancamentos/admin/form.html')


def save(_handler, lancamento_id=None, **lancamento_properties):
    cmd = facade.save_lancamento_cmd(**lancamento_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'lancamento': cmd.form}

        return TemplateResponse(context, 'lancamentos/admin/form.html')
    _handler.redirect(router.to_path(admin))

