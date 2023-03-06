#!/usr/bin/python3
"""Amenity module."""
from models import *


class Amenity(BaseModel):
    """Represents amenities disbursed to users.

    Attributes:
        BaseModel ('obj':'class'): Superclass

    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialise instances."""
        super().__init__(*args, **kwargs)
