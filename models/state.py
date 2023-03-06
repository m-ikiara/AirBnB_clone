#!/usr/bin/python3
"""State module."""
from models import *


class State(BaseModel):
    """Represent a State.

    Attributes:
        BaseModel ('obj':'class'): Superclass

    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a state."""
        super(State, self).__init__(*args, **kwargs)
