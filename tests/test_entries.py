# tests/test_entries.py

# For unit testing of entries

# standard unittest
import unittest
# import Entry classe from models
from app.models import Entry

class TestDiaryEntry(unittest.TestCase):
    """test for successful and unsuccessful entry addition"""
    def setUp(self):
        self.ent = Entry()
    def test_entry_adding_success(self):
        """returns True if entry addition was successful"""
        result = self.ent.add_entry("At Russia", "some good description of world cup experience")
        self.assertEqual(True, result)

    def test_entry_adding_failure(self):
    	"""returns False if an entry addition failed"""
    	result = self.ent.add_entry("title", "some")
    	self.assertFalse(False, result)
        