"""
Composition of Decorators
-------------------------
Function decorators are simply wrappers to existing functions. Putting the
ideas mentioned above together, we can build a decorator. In this example
let's consider a function that wraps the string output of another function
by p tags.
"""


def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))

    return func_wrapper


my_get_text = p_decorate(get_text)

print my_get_text("John")

# Python's Decorator Syntax
# -------------------------
# Python makes creating and using decorators a bit cleaner and nicer for the
#  programmer through some syntactic sugar To decorate get_text we don't
# have to get_text = p_decorator(get_text) There is a neat shortcut for
# that, which is to mention the name of the decorating function before the
# function to be decorated. The name of the decorator should be perpended
# with an @ symbol.
#

@p_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text("John")