# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from filme_app import facade
from routes.filmes.admin import new, edit


def delete(_handler, filmes_id):
    facade.delete_filmes_cmd(filmes_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_filmess_cmd()
    filmess = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.filmes_short_form()

    def short_filmes_dict(filmes):
        filmes_dct = short_form.fill_with_model(filmes)
        filmes_dct['edit_path'] = router.to_path(edit_path, filmes_dct['id'])
        filmes_dct['delete_path'] = router.to_path(delete_path, filmes_dct['id'])
        return filmes_dct

    short_filmess = [short_filmes_dict(filmes) for filmes in filmess]
    context = {'filmess': short_filmess,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

