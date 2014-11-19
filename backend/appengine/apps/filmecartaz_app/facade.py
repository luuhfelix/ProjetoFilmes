# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from filmecartaz_app.commands import ListCartazCommand, SaveCartazCommand, UpdateCartazCommand, \
    CartazPublicForm, CartazDetailForm, CartazShortForm


def save_cartaz_cmd(**cartaz_properties):
    """
    Command to save Cartaz entity
    :param cartaz_properties: a dict of properties to save on model
    :return: a Command that save Cartaz, validating and localizing properties received as strings
    """
    return SaveCartazCommand(**cartaz_properties)


def update_cartaz_cmd(cartaz_id, **cartaz_properties):
    """
    Command to update Cartaz entity with id equals 'cartaz_id'
    :param cartaz_properties: a dict of properties to update model
    :return: a Command that update Cartaz, validating and localizing properties received as strings
    """
    return UpdateCartazCommand(cartaz_id, **cartaz_properties)


def list_cartazs_cmd():
    """
    Command to list Cartaz entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListCartazCommand()


def cartaz_detail_form(**kwargs):
    """
    Function to get Cartaz's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return CartazDetailForm(**kwargs)


def cartaz_short_form(**kwargs):
    """
    Function to get Cartaz's short form. just a subset of cartaz's properties
    :param kwargs: form properties
    :return: Form
    """
    return CartazShortForm(**kwargs)

def cartaz_public_form(**kwargs):
    """
    Function to get Cartaz'spublic form. just a subset of cartaz's properties
    :param kwargs: form properties
    :return: Form
    """
    return CartazPublicForm(**kwargs)


def get_cartaz_cmd(cartaz_id):
    """
    Find cartaz by her id
    :param cartaz_id: the cartaz id
    :return: Command
    """
    return NodeSearch(cartaz_id)


def delete_cartaz_cmd(cartaz_id):
    """
    Construct a command to delete a Cartaz
    :param cartaz_id: cartaz's id
    :return: Command
    """
    return DeleteNode(cartaz_id)

