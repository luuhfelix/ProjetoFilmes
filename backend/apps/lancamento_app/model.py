# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Lancamento(Node):
    titulo = ndb.StringProperty(required=True)
    lancamento = ndb.DateProperty(required=True)
    de = ndb.StringProperty(required=True)
    genero = ndb.StringProperty(required=True)
    com = ndb.StringProperty(required=True)

