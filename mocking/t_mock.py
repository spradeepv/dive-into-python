class Class1(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print "Pradeep"
        return "Pradeep"


class TClass1(Class1):
    def test_get_name(self):
        name = self.get_name()
        print name

t = TClass1("Test")
t.test_get_name()