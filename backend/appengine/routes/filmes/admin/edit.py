# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from filme_app import facade
from routes.filmes import admin


@no_csrf
def index(filmes_id):
    filmes = facade.get_filmes_cmd(filmes_id)()
    detail_form = facade.filmes_detail_form()
    context = {'save_path': router.to_path(save, filmes_id), 'filmes': detail_form.fill_with_model(filmes)}
    return TemplateResponse(context, 'filmes/admin/form.html')


def save(_handler, filmes_id, **filmes_properties):
    cmd = facade.update_filmes_cmd(filmes_id, **filmes_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'filmes': cmd.form}

        return TemplateResponse(context, 'filmes/admin/form.html')
    _handler.redirect(router.to_path(admin))

