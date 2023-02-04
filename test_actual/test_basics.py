import unittest
from ed_utils.decorators import *
from ed_utils.timeout import timeout

class TestThings(unittest.TestCase):

    @number("1.1")
    @timeout()
    @advanced()
    def test_basic(self):
        print("HI")
        self.assertEqual(True, False)

    @number("1.2")
    @timeout()
    @weight(3)
    def test_basic_2(self):
        print("HI AGAIN")
        self.assertEqual(True, True)

    @number("1.3")
    @timeout()
    @advanced()
    @hide_errors("You can't see me")
    def test_basic_3(self):
        print("HI ALWAYS\n")
        self.assertEqual(True, False)

    @number("2.1")
    @timeout()
    @visibility(visibility.VISIBILITY_HIDDEN)
    def test_more(self):
        self.assertEqual(True, False)

    @number("2.2")
    @timeout()
    @visibility(visibility.VISIBILITY_PRIVATE)
    def test_more_2(self):
        self.assertEqual(True, False)

    @number("2.3")
    @timeout()
    @visibility(visibility.VISIBILITY_SHOW)
    def test_more_3(self):
        self.assertEqual(True, True)
