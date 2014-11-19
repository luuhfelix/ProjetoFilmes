# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from filme_app import facade
from routes.filmes import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'filmes/admin/form.html')


def save(_handler, filmes_id=None, **filmes_properties):
    cmd = facade.save_filmes_cmd(**filmes_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'filmes': cmd.form}

        return TemplateResponse(context, 'filmes/admin/form.html')
    _handler.redirect(router.to_path(admin))

