def usage(cls):
    """
    The point is that the underlying object becomes immutable, while the
    wrapper becomes mutable.
    Basically, just to prevent the binding of state to the namespaces of the object.
    """
    obj = cls.__new__()
    mutable = Mutator(obj)
    mutable.state = obj.__init__()

    result = mutable.method() # --> result = result = obj.method(mutable.state)




import copy

class MyClass(object):
    """
    An example of a FunctionalClass.
    Does not use the builtin __init__, because it needs to violate those rules.
    This could be done with a Metaclass, but I don't want that complexity yet.
    """
    def __new__(cls):
        state = cls.init()
        self = object.__init__(cls)
        self.__state__ = 

    @classmethod
    def init(cls):
        state = {'data': 'abc'}
        return state

def the_idea(cls):
    """ NOT drafting this using the 'external' namespace operator, obj|state

    What is *actually* novel about this?
        Only that the binding of state into the object is localized into the
    the function that the object is initialized in.
    So, in native python, an initialized object has two things:
        (1) its own namespace (chained on top of the class)
        (2) its own state (which is placed into the object's namespace)

    This strategy has an initialized object:
        (1) its own namespace (chained on top of the class)
        (2) its own state (placed into the containing functions namespace)
    """
    # obj = cls()
    obj = cls.__new__()
    obj.state = cls.__init__()

    obj.method = partial(obj.method, obj.state)
    result = obj.method()
