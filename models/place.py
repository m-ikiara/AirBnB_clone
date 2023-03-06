#!/usr/bin/python3
"""Place module."""
from models import *


class Place(BaseModel):
    """Represent a Place.

    Attributes:
        BaseModel ('obj':'class'): Superclass

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenities = [""]

    def __init__(self, *args, **kwargs):
        """Initialize a Place instance."""
        super().__init__()
