#!/usr/bin/python3
"""Create a Blueprint instance with URL prefix /api/v1"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

if app_views is not None:
    from api.v1.views.index import *
    from api.v1.views.states import *
    from api.v1.views.cities import *
    from api.v1.views.amenities import *
    from api.v1.views.users import *
    from api.v1.views.places import *
    from api.v1.views.places_reviews import *
    from api.v1.views.places_amenities import *

"""Wildcard import of everything in the package api.v1.views.index
PEP8 will complain about it, but it's normal and this file (v1/views/__init__.py) won't be checked."""
from api.v1.views.index import *
