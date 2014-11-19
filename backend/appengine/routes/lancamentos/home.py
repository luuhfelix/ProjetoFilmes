# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from filme_app import facade
from routes.filmes import admin, rest


@login_not_required
@no_csrf
def index():
    cmd = facade.list_lancamentos_cmd()
    lancamentos = cmd()
    public_form = facade.lancamento_public_form()
    lancamento_public_dcts = [public_form.fill_with_model(lancamento) for lancamento in lancamentos]
    context = {'lancamentos': lancamento_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

