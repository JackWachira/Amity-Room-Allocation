import unittest
from utils import Fileparser

"""Unit tests for testing various functions in File Parser class
"""


class File_Parsing_Tests(unittest.TestCase):

    """Tests whether functions returns the correct list of rows of a txt file.
    """

    def test_get_line_contents(self):
        parser = Fileparser.Fileparser(
            "/Users/JackMwangi/Documents/Python Workspace/Checkpoint1/tests/testinput.txt")
        list_allocations = parser.readfile()
        self.assertEqual(len(list_allocations), 3)