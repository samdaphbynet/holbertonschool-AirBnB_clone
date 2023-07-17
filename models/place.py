#!/usr/bin/python3
"""place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
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
    amenity_ids = ""

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.city_id = kwargs.get("city_id", "")
    #     self.user_id = kwargs.get("user_id", "")
    #     self.name = kwargs.get("name", "")
    #     self.description = kwargs.get("description", "")
    #     self.number_rooms = kwargs.get("number_rooms", "")
    #     self.number_bathrooms = kwargs.get("number.bathrooms", "")
    #     self.max_guest = kwargs.get("max_guest", "")
    #     self.price_by_night = kwargs.get("price_by_night", "")
    #     self.latitude = kwargs.get("latitude", "")
    #     self.longitude = kwargs.get("longitude", "")
    #     self.amenity_ids = kwargs.get("amenity_ids", "")
