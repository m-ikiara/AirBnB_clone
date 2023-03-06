#!/usr/bin/python3
"""City module."""
from models import *


class City(BaseModel):
    """Represent a city.

    Attributes:
        BaseModel ('obj':'class'): Superclass

    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize City instances."""
        super().__init__(*args, **kwargs)
