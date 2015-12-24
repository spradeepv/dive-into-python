import mock
import unittest

class Class1(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print "Pradeep"
        return "Pradeep"


class TestClass1(unittest.TestCase, Class1):

    def setUp(self):
        print "Start"

    def test_get_name(self):
        name = self.get_name()
        self.assertEquals("Pradeep", name)
