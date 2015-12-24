"""
Passing arguments to decorators
------------------------------
Looking back at the example before the one above, you can notice how
redundant the decorators in the example are. 3 decorators(div_decorate,
p_decorate, strong_decorate) each with the same functionality but wrapping
the string with different tags. We can definitely do much better than that.
Why not have a more general implementation for one that takes the tag to
wrap with as a string? Yes please!
"""

def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    return "Hello "+name

print get_text("John")