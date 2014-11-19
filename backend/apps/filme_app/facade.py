# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from filme_app.commands import ListFilmesCommand, SaveFilmesCommand, UpdateFilmesCommand, \
    FilmesPublicForm, FilmesDetailForm, FilmesShortForm


def save_filmes_cmd(**filmes_properties):
    """
    Command to save Filmes entity
    :param filmes_properties: a dict of properties to save on model
    :return: a Command that save Filmes, validating and localizing properties received as strings
    """
    return SaveFilmesCommand(**filmes_properties)


def update_filmes_cmd(filmes_id, **filmes_properties):
    """
    Command to update Filmes entity with id equals 'filmes_id'
    :param filmes_properties: a dict of properties to update model
    :return: a Command that update Filmes, validating and localizing properties received as strings
    """
    return UpdateFilmesCommand(filmes_id, **filmes_properties)


def list_filmess_cmd():
    """
    Command to list Filmes entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListFilmesCommand()


def filmes_detail_form(**kwargs):
    """
    Function to get Filmes's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return FilmesDetailForm(**kwargs)


def filmes_short_form(**kwargs):
    """
    Function to get Filmes's short form. just a subset of filmes's properties
    :param kwargs: form properties
    :return: Form
    """
    return FilmesShortForm(**kwargs)

def filmes_public_form(**kwargs):
    """
    Function to get Filmes'spublic form. just a subset of filmes's properties
    :param kwargs: form properties
    :return: Form
    """
    return FilmesPublicForm(**kwargs)


def get_filmes_cmd(filmes_id):
    """
    Find filmes by her id
    :param filmes_id: the filmes id
    :return: Command
    """
    return NodeSearch(filmes_id)


def delete_filmes_cmd(filmes_id):
    """
    Construct a command to delete a Filmes
    :param filmes_id: filmes's id
    :return: Command
    """
    return DeleteNode(filmes_id)

