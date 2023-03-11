#!/usr/bin/python3
'''
This is the 'test_base_model' module.
test_base_model uses unittest to test the 'models/base_model' module.
'''
import unittest
from models import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class
    """
    def setUp(self):
        """sets up objects for testing later
        """
        self.test_model1 = BaseModel()
        self.test_model2 = BaseModel()

    def test_basic_setup(self):
        """test for to_json method of BaseModel class
        """
        self.assertTrue(hasattr(self.test_model1, "id"))
        self.assertTrue(hasattr(self.test_model1, "__class__"))
        self.assertTrue(hasattr(self.test_model1, "created_at"))
        self.assertTrue(hasattr(self.test_model1, "updated_at"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        self.assertTrue(m1c != m2c)

    def test_types(self):
        """testing attributes to ensure proper typing
        """
        self.assertTrue(type(self.test_model1.id) is str)
        self.assertTrue(type(self.test_model1.__class__) is type)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        m1u = self.test_model1.updated_at
        m2u = self.test_model2.updated_at
        self.assertTrue(type(m1c) is datetime.datetime)
        self.assertTrue(type(m2c) is datetime.datetime)
        self.assertTrue(type(m1u) is datetime.datetime)
        self.assertTrue(type(m2u) is datetime.datetime)

    def test_save(self):
        """testing whether save updates the updated_at attribute
        """
        m1u = self.test_model1.updated_at
        self.test_model1.save()
        m1u_saved = self.test_model1.updated_at
        self.assertFalse(m1u == m1u_saved)

    def test_to_json(self):
        """tests to_json method with diffs in output & in-memory objects
        """
        testmodelid = self.test_model1.id
        jsondict = self.test_model1.to_json()
        self.assertNotEqual(jsondict, self.test_model1.__dict__)
        self.assertEqual(jsondict["id"], self.test_model1.__dict__["id"])
        self.assertNotEqual(jsondict["created_at"],
                            self.test_model1.__dict__["created_at"])
        self.assertNotEqual(type(jsondict["created_at"]),
                            type(self.test_model1.__dict__["created_at"]))

if __name__ == '__main__':
    unittest.main()
