#!/usr/bin/python3
"""Review module."""
from models import *


class Review(BaseModel):
    """Review the current objects.

    Attributes:
        BaseModel ('obj':'class'): Superclass

    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a Review instance."""
        super().__init__(*args, **kwargs)
