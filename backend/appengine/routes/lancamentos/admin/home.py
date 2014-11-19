# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from lancamento_app import facade
from routes.lancamentos.admin import new, edit


def delete(_handler, lancamento_id):
    facade.delete_lancamento_cmd(lancamento_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_lancamentos_cmd()
    lancamentos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.lancamento_short_form()

    def short_lancamento_dict(lancamento):
        lancamento_dct = short_form.fill_with_model(lancamento)
        lancamento_dct['edit_path'] = router.to_path(edit_path, lancamento_dct['id'])
        lancamento_dct['delete_path'] = router.to_path(delete_path, lancamento_dct['id'])
        return lancamento_dct

    short_lancamentos = [short_lancamento_dict(lancamento) for lancamento in lancamentos]
    context = {'lancamentos': short_lancamentos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

