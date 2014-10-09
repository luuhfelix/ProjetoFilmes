# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from filme_app.model import Filme

class FilmePublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Filme
    _include = [Filme.titulo, 
                Filme.lancamento, 
                Filme.de, 
                Filme.genero, 
                Filme.com]


class FilmeForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Filme
    _include = [Filme.titulo, 
                Filme.lancamento, 
                Filme.de, 
                Filme.genero, 
                Filme.com]


class FilmeDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Filme
    _include = [Filme.de, 
                Filme.genero, 
                Filme.creation, 
                Filme.lancamento, 
                Filme.titulo, 
                Filme.com]


class FilmeShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Filme
    _include = [Filme.de, 
                Filme.genero, 
                Filme.creation, 
                Filme.lancamento, 
                Filme.titulo, 
                Filme.com]


class SaveFilmeCommand(SaveCommand):
    _model_form_class = FilmeForm


class UpdateFilmeCommand(UpdateNode):
    _model_form_class = FilmeForm


class ListFilmeCommand(ModelSearchCommand):
    def __init__(self):
        super(ListFilmeCommand, self).__init__(Filme.query_by_creation())

