# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from filmecartaz_app import facade
from routes.filmecartazs import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'filmecartazs/admin/form.html')


def save(_handler, cartaz_id=None, **cartaz_properties):
    cmd = facade.save_cartaz_cmd(**cartaz_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'cartaz': cmd.form}

        return TemplateResponse(context, 'filmecartazs/admin/form.html')
    _handler.redirect(router.to_path(admin))

