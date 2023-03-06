#!/usr/bin/python3
"""User module."""
from models import *


class User(BaseModel):
    """Represent a User.

    Attributes:
        BaseModel ('obj':'class'): Superclass

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a User instance."""
        super().__init__(*args, **kwargs)
