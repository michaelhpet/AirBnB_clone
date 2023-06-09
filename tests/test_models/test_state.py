#!/usr/bin/python3
"""Module for State tests."""
import os
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
from models import storage

objects_path = os.path.join(os.path.abspath("objects.json"))


class TestState(unittest.TestCase):
    """Define tests for State class."""

    def test_instance(self):
        obj = State()
        self.assertIsInstance(obj, State)
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(isinstance(obj, BaseModel))

    def test_instance_with_none(self):
        obj = State(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_stored_instances(self):
        for _ in range(5):
            obj = State()
            obj.save()
        objs = storage.all()
        for key in objs:
            self.assertIsInstance(objs[key], (BaseModel, State))

    def test_attributes(self):
        obj = State()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertIsNotNone(obj.name)

    def test_id_is_str(self):
        obj = State()
        self.assertIsInstance(obj.id, str)

    def test_name_is_str(self):
        obj = State()
        self.assertIsInstance(obj.name, str)

    def test_created_at_is_datetime(self):
        obj = State()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_is_datetime(self):
        obj = State()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_id_is_unique(self):
        obj1 = State()
        obj2 = State()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_serial_created_at(self):
        obj1 = State()
        obj2 = State()
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        obj1_timestamp = obj1.created_at.timestamp()
        obj2_timestamp = obj2.created_at.timestamp()
        self.assertLess(obj1_timestamp, obj2_timestamp)

    def test_serial_updated_at(self):
        obj1 = State()
        obj2 = State()
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)
        obj1_timestamp = obj1.updated_at.timestamp()
        obj2_timestamp = obj2.updated_at.timestamp()
        self.assertLess(obj1_timestamp, obj2_timestamp)

    def test_str(self):
        obj = State()
        obj.id = "ABC"
        obj_sub_str = "[State] (ABC)"
        self.assertIn(obj_sub_str, obj.__str__())

    def test_to_dict(self):
        obj = State()
        to_dict_result = obj.to_dict()
        self.assertIsInstance(to_dict_result, dict)

        values = obj.__dict__
        for key in values:
            if key not in ["created_at", "updated_at"]:
                self.assertIn(values[key], to_dict_result.values())

    def test_instance_with_args(self):
        obj = State("ABC", "124")
        self.assertNotEqual("ABC", obj.id)
        self.assertNotEqual("124", obj.id)
        self.assertNotIn("ABC", obj.__dict__.values())
        self.assertNotIn("124", obj.__dict__.values())

    def test_instance_with_kwargs(self):
        obj = State(id="ABC", name="Lagos")
        self.assertEqual("ABC", obj.id)
        self.assertEqual("Lagos", obj.name)

    def test_instance_with_args_kwargs(self):
        obj = State("ABC", id="124", name="Kigali")
        self.assertNotEqual("ABC", obj.id)
        self.assertEqual("124", obj.id)
        self.assertEqual("Kigali", obj.name)
        self.assertNotIn("ABC", obj.__dict__.values())
        self.assertIn("124", obj.__dict__.values())
        self.assertIn("Kigali", obj.__dict__.values())

    def tearDown(self):
        try:
            os.remove(objects_path)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
