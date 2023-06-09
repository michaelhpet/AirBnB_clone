#!/usr/bin/python3
"""Module for Amenity tests."""
import os
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage

objects_path = os.path.join(os.path.abspath("objects.json"))


class TestAmenity(unittest.TestCase):
    """Define tests for Amenity class."""

    def test_instance(self):
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(isinstance(obj, BaseModel))

    def test_instance_with_none(self):
        obj = Amenity(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_stored_instances(self):
        for _ in range(5):
            obj = Amenity()
            obj.save()
        objs = storage.all()
        for key in objs:
            self.assertIsInstance(objs[key], (BaseModel, Amenity))

    def test_attributes(self):
        obj = Amenity()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertIsNotNone(obj.name)

    def test_id_is_str(self):
        obj = Amenity()
        self.assertIsInstance(obj.id, str)

    def test_name_is_str(self):
        obj = Amenity()
        self.assertIsInstance(obj.name, str)

    def test_created_at_is_datetime(self):
        obj = Amenity()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_is_datetime(self):
        obj = Amenity()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_id_is_unique(self):
        obj1 = Amenity()
        obj2 = Amenity()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_serial_created_at(self):
        obj1 = Amenity()
        obj2 = Amenity()
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        obj1_timestamp = obj1.created_at.timestamp()
        obj2_timestamp = obj2.created_at.timestamp()
        self.assertLess(obj1_timestamp, obj2_timestamp)

    def test_serial_updated_at(self):
        obj1 = Amenity()
        obj2 = Amenity()
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)
        obj1_timestamp = obj1.updated_at.timestamp()
        obj2_timestamp = obj2.updated_at.timestamp()
        self.assertLess(obj1_timestamp, obj2_timestamp)

    def test_str(self):
        obj = Amenity()
        obj.id = "ABC"
        obj_sub_str = "[Amenity] (ABC)"
        self.assertIn(obj_sub_str, obj.__str__())

    def test_to_dict(self):
        obj = Amenity()
        to_dict_result = obj.to_dict()
        self.assertIsInstance(to_dict_result, dict)

        values = obj.__dict__
        for key in values:
            if key not in ["created_at", "updated_at"]:
                self.assertIn(values[key], to_dict_result.values())

    def test_instance_with_args(self):
        obj = Amenity("ABC", "124")
        self.assertNotEqual("ABC", obj.id)
        self.assertNotEqual("124", obj.id)
        self.assertNotIn("ABC", obj.__dict__.values())
        self.assertNotIn("124", obj.__dict__.values())

    def test_instance_with_kwargs(self):
        obj = Amenity(id="ABC", name="Hello World")
        self.assertEqual("ABC", obj.id)
        self.assertEqual("Hello World", obj.name)

    def test_instance_with_args_kwargs(self):
        obj = Amenity("ABC", id="124", name="Hello World")
        self.assertNotEqual("ABC", obj.id)
        self.assertEqual("124", obj.id)
        self.assertEqual("Hello World", obj.name)
        self.assertNotIn("ABC", obj.__dict__.values())
        self.assertIn("124", obj.__dict__.values())
        self.assertIn("Hello World", obj.__dict__.values())

    def tearDown(self):
        try:
            os.remove(objects_path)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
