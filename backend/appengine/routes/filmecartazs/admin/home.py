# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from filmecartaz_app import facade
from routes.filmecartazs.admin import new, edit


def delete(_handler, cartaz_id):
    facade.delete_cartaz_cmd(cartaz_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_cartazs_cmd()
    cartazs = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.cartaz_short_form()

    def short_cartaz_dict(cartaz):
        cartaz_dct = short_form.fill_with_model(cartaz)
        cartaz_dct['edit_path'] = router.to_path(edit_path, cartaz_dct['id'])
        cartaz_dct['delete_path'] = router.to_path(delete_path, cartaz_dct['id'])
        return cartaz_dct

    short_cartazs = [short_cartaz_dict(cartaz) for cartaz in cartazs]
    context = {'cartazs': short_cartazs,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

