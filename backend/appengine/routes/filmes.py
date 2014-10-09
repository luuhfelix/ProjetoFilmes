from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms import base
from gaeforms.base import Form
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node, Arc
from gaepermission.decorator import login_not_required
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
'''
@login_not_required
@no_csrf
def index():
    query = Filme.query().order(Filme.lancamento)
    filme_lista = query.fetch()
    filme_form = FilmeFormTable()
    filme_lista = [filme_form.fill_with_model(filme) for filme in filme_lista]
    editar_form_path=router.to_path(editar_form)
    delete_path=router.to_path(delete)
    for filme in filme_lista:
        filme['edit_path'] = '%s/%s' %(editar_form_path,filme['id'])
        filme['delete_path'] = '%s/%s' %(delete_path,filme['id'])
    contexto={'filme_lista': filme_lista,'form_path': router.to_path(form)}
    return TemplateResponse(contexto)
'''

@no_csrf
def index(_logged_user):
    chave_do_usuario = _logged_user.key
    query= AutorArco.query(AutorArco.origin==chave_do_usuario)
    autor_arcos = query.fetch()
    chave_de_filmes = [arco.destination for arco in autor_arcos]
    filme_lista = ndb.get_multi(chave_de_filmes)
    filme_form = FilmeFormTable()
    filme_lista = [filme_form.fill_with_model(filme) for filme in filme_lista]
    editar_form_path=router.to_path(editar_form)
    delete_path=router.to_path(delete)
    for filme in filme_lista:
        filme['edit_path'] = '%s/%s' %(editar_form_path,filme['id'])
        filme['delete_path'] = '%s/%s' %(delete_path,filme['id'])
    contexto={'filme_lista': filme_lista,'form_path': router.to_path(form)}
    return TemplateResponse(contexto)

'''
def delete(filme_id):
    chave = ndb.Key(Filme,int(filme_id))
    chave.delete()
    return RedirectResponse(router.to_path(index))
'''

def delete(filme_id):
    chave = ndb.Key(Filme,int(filme_id))
    chave.delete()
    query = AutorArco.find_origins(chave)
    chaves_dos_arcos = query.fetch(keys_only=True)
    ndb.delete_multi(chaves_dos_arcos)
    return RedirectResponse(router.to_path(index))


@no_csrf
def editar_form(filme_id):
    filme_id = int(filme_id)
    filme = Filme.get_by_id(filme_id)
    filme_form = FilmeForm()
    filme_form.fill_with_model(filme)
    contexto={'salvar_path': router.to_path(editar,filme_id),'filme':filme_form}
    return TemplateResponse(contexto, 'filmes/form.html')


def editar(filme_id,**propriedades):
    filme_id = int(filme_id)
    filme = Filme.get_by_id(filme_id)
    filme_form=FilmeForm(**propriedades)
    errors = filme_form.validate()
    if errors:
        contexto={'salvar_path': router.to_path(salvar),
                  'errors':errors,'filme':filme_form}
        return TemplateResponse(contexto,'filmes/form.html')
    else:
        filme=filme_form.fill_model(filme)
        filme.put()
        return RedirectResponse(router.to_path(index))


@no_csrf
def form():
    contexto={'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)
'''
@no_csrf
def salvar(**propriedades):
    filme_form=FilmeForm(**propriedades)
    errors = filme_form.validate()
    if errors:
        contexto={'salvar_path': router.to_path(salvar),
                  'errors':errors,'filme':filme_form}
        return TemplateResponse(contexto,'filmes/form.html')
    else:
        filme=filme_form.fill_model()
        filme.put()
        return RedirectResponse(router.to_path(index))
'''

@no_csrf
def salvar(_logged_user,**propriedades):
    filme_form=FilmeForm(**propriedades)
    errors = filme_form.validate()
    if errors:
        contexto={'salvar_path': router.to_path(salvar),
                  'errors':errors,'filme':filme_form}
        return TemplateResponse(contexto,'filmes/form.html')
    else:
        filme=filme_form.fill_model()
        chave_de_filmes =  filme.put()
        chave_do_usuario = _logged_user.key
        autor_arco = AutorArco(origin=chave_do_usuario,destination=chave_de_filmes)
        autor_arco.put()
        return RedirectResponse(router.to_path(index))

class Filme(Node):
    titulo=ndb.StringProperty(required=True)
    lancamento=ndb.DateProperty(required=True)
    de=ndb.StringProperty(required=True)
    genero=ndb.StringProperty(required=True)
    com=ndb.StringProperty(required=True)

class AutorArco(Arc):
    origin = ndb.KeyProperty(required=True)
    destination = ndb.KeyProperty(Filme,required=True)

class FilmeFormTable(ModelForm):
    _model_class = Filme
    _include = [Filme.titulo,Filme.lancamento,Filme.de,Filme.genero,Filme.com]

class FilmeForm(ModelForm):
    _model_class = Filme
    _include = [Filme.titulo,Filme.lancamento,Filme.de,Filme.genero,Filme.com]






