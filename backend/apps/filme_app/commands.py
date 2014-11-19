# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from filme_app.model import Filmes

class FilmesPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Filmes
    _include = [Filmes.titulo, 
                Filmes.lancamento, 
                Filmes.de, 
                Filmes.genero, 
                Filmes.com]


class FilmesForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Filmes
    _include = [Filmes.titulo, 
                Filmes.lancamento, 
                Filmes.de, 
                Filmes.genero, 
                Filmes.com]


class FilmesDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Filmes
    _include = [Filmes.de, 
                Filmes.genero, 
                Filmes.creation, 
                Filmes.lancamento, 
                Filmes.titulo, 
                Filmes.com]


class FilmesShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Filmes
    _include = [Filmes.de, 
                Filmes.genero, 
                Filmes.creation, 
                Filmes.lancamento, 
                Filmes.titulo, 
                Filmes.com]


class SaveFilmesCommand(SaveCommand):
    _model_form_class = FilmesForm


class UpdateFilmesCommand(UpdateNode):
    _model_form_class = FilmesForm


class ListFilmesCommand(ModelSearchCommand):
    def __init__(self):
        super(ListFilmesCommand, self).__init__(Filmes.query_by_creation())

