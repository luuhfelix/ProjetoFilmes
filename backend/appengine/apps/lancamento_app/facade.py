# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from lancamento_app.commands import ListLancamentoCommand, SaveLancamentoCommand, UpdateLancamentoCommand, \
    LancamentoPublicForm, LancamentoDetailForm, LancamentoShortForm


def save_lancamento_cmd(**lancamento_properties):
    """
    Command to save Lancamento entity
    :param lancamento_properties: a dict of properties to save on model
    :return: a Command that save Lancamento, validating and localizing properties received as strings
    """
    return SaveLancamentoCommand(**lancamento_properties)


def update_lancamento_cmd(lancamento_id, **lancamento_properties):
    """
    Command to update Lancamento entity with id equals 'lancamento_id'
    :param lancamento_properties: a dict of properties to update model
    :return: a Command that update Lancamento, validating and localizing properties received as strings
    """
    return UpdateLancamentoCommand(lancamento_id, **lancamento_properties)


def list_lancamentos_cmd():
    """
    Command to list Lancamento entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListLancamentoCommand()


def lancamento_detail_form(**kwargs):
    """
    Function to get Lancamento's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return LancamentoDetailForm(**kwargs)


def lancamento_short_form(**kwargs):
    """
    Function to get Lancamento's short form. just a subset of lancamento's properties
    :param kwargs: form properties
    :return: Form
    """
    return LancamentoShortForm(**kwargs)

def lancamento_public_form(**kwargs):
    """
    Function to get Lancamento'spublic form. just a subset of lancamento's properties
    :param kwargs: form properties
    :return: Form
    """
    return LancamentoPublicForm(**kwargs)


def get_lancamento_cmd(lancamento_id):
    """
    Find lancamento by her id
    :param lancamento_id: the lancamento id
    :return: Command
    """
    return NodeSearch(lancamento_id)


def delete_lancamento_cmd(lancamento_id):
    """
    Construct a command to delete a Lancamento
    :param lancamento_id: lancamento's id
    :return: Command
    """
    return DeleteNode(lancamento_id)

