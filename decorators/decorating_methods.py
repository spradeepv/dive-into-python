"""
In Python, methods are functions that expect their first parameter to be a
reference to the current object. We can build decorators for methods the
same way, while taking self into consideration in the wrapper function.
"""


def p_decorate(func):
    def func_wrapper(self):
        return "<p>{0}</p>".format(func(self))

    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.family


my_person = Person()
print my_person.get_fullname()

# A much better approach would be to make our decorator useful for functions
# and methods alike. This can be done by putting *args and **kwargs as
# parameters for the wrapper, then it can accept any arbitrary number of
# arguments and keyword arguments.

def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()
print my_person.get_fullname()
