#!/usr/bin/python3
"""
Amenity module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class
    """

    name = ""
    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs
