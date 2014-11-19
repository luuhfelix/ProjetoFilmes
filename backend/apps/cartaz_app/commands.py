# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from cartaz_app.model import Cartaz

class CartazPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Cartaz
    _include = [Cartaz.titulo, 
                Cartaz.lancamento, 
                Cartaz.de, 
                Cartaz.genero, 
                Cartaz.com]


class CartazForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Cartaz
    _include = [Cartaz.titulo, 
                Cartaz.lancamento, 
                Cartaz.de, 
                Cartaz.genero, 
                Cartaz.com]


class CartazDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Cartaz
    _include = [Cartaz.de, 
                Cartaz.genero, 
                Cartaz.creation, 
                Cartaz.lancamento, 
                Cartaz.titulo, 
                Cartaz.com]


class CartazShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Cartaz
    _include = [Cartaz.de, 
                Cartaz.genero, 
                Cartaz.creation, 
                Cartaz.lancamento, 
                Cartaz.titulo, 
                Cartaz.com]


class SaveCartazCommand(SaveCommand):
    _model_form_class = CartazForm


class UpdateCartazCommand(UpdateNode):
    _model_form_class = CartazForm


class ListCartazCommand(ModelSearchCommand):
    def __init__(self):
        super(ListCartazCommand, self).__init__(Cartaz.query_by_creation())

