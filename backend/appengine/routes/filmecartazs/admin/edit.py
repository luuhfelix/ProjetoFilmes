# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from filmecartaz_app import facade
from routes.filmecartazs import admin


@no_csrf
def index(cartaz_id):
    cartaz = facade.get_cartaz_cmd(cartaz_id)()
    detail_form = facade.cartaz_detail_form()
    context = {'save_path': router.to_path(save, cartaz_id), 'cartaz': detail_form.fill_with_model(cartaz)}
    return TemplateResponse(context, 'filmecartazs/admin/form.html')


def save(_handler, cartaz_id, **cartaz_properties):
    cmd = facade.update_cartaz_cmd(cartaz_id, **cartaz_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'cartaz': cmd.form}

        return TemplateResponse(context, 'filmecartazs/admin/form.html')
    _handler.redirect(router.to_path(admin))

