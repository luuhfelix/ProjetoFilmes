# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from lancamento_app.model import Lancamento

class LancamentoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Lancamento
    _include = [Lancamento.titulo, 
                Lancamento.lancamento, 
                Lancamento.de, 
                Lancamento.genero, 
                Lancamento.com]


class LancamentoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Lancamento
    _include = [Lancamento.titulo, 
                Lancamento.lancamento, 
                Lancamento.de, 
                Lancamento.genero, 
                Lancamento.com]


class LancamentoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Lancamento
    _include = [Lancamento.de, 
                Lancamento.genero, 
                Lancamento.creation, 
                Lancamento.lancamento, 
                Lancamento.titulo, 
                Lancamento.com]


class LancamentoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Lancamento
    _include = [Lancamento.de, 
                Lancamento.genero, 
                Lancamento.creation, 
                Lancamento.lancamento, 
                Lancamento.titulo, 
                Lancamento.com]


class SaveLancamentoCommand(SaveCommand):
    _model_form_class = LancamentoForm


class UpdateLancamentoCommand(UpdateNode):
    _model_form_class = LancamentoForm


class ListLancamentoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListLancamentoCommand, self).__init__(Lancamento.query_by_creation())

