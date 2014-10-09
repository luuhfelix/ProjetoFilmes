# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from filme_app.commands import ListFilmeCommand, SaveFilmeCommand, UpdateFilmeCommand, \
    FilmePublicForm, FilmeDetailForm, FilmeShortForm


def save_filme_cmd(**filme_properties):
    """
    Command to save Filme entity
    :param filme_properties: a dict of properties to save on model
    :return: a Command that save Filme, validating and localizing properties received as strings
    """
    return SaveFilmeCommand(**filme_properties)


def update_filme_cmd(filme_id, **filme_properties):
    """
    Command to update Filme entity with id equals 'filme_id'
    :param filme_properties: a dict of properties to update model
    :return: a Command that update Filme, validating and localizing properties received as strings
    """
    return UpdateFilmeCommand(filme_id, **filme_properties)


def list_filmes_cmd():
    """
    Command to list Filme entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListFilmeCommand()


def filme_detail_form(**kwargs):
    """
    Function to get Filme's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return FilmeDetailForm(**kwargs)


def filme_short_form(**kwargs):
    """
    Function to get Filme's short form. just a subset of filme's properties
    :param kwargs: form properties
    :return: Form
    """
    return FilmeShortForm(**kwargs)

def filme_public_form(**kwargs):
    """
    Function to get Filme'spublic form. just a subset of filme's properties
    :param kwargs: form properties
    :return: Form
    """
    return FilmePublicForm(**kwargs)


def get_filme_cmd(filme_id):
    """
    Find filme by her id
    :param filme_id: the filme id
    :return: Command
    """
    return NodeSearch(filme_id)


def delete_filme_cmd(filme_id):
    """
    Construct a command to delete a Filme
    :param filme_id: filme's id
    :return: Command
    """
    return DeleteNode(filme_id)

