"""

Draft notes of an idea, placing 'state' on an extra layer around objects.
So that we can keep their normal namespace pure and immutable.
"""

class HasState(object):
    """
    """
    # __state__ : parallels __dict__
    # >> : operator to access state version
    def __new__(cls, *args, **kwargs):
        state = cls.__init__(*args, **kwargs)

# myobj = MyClass(...)
# myobj >> 'attr'
