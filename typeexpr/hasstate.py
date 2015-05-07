"""

Tentative idea:
    class --> instance
    class & HasState --> instance

? Does it make sense to define instances as *just* another class, except
that they inherit from the base class "HasState" - and
"HasState" defines __init__ and __state__ (?__dict__?)
"""

class HasState(object):
    @abstractmethod
    def __init__(cls, ):
        """
        __init__(X, *, **) -> 
        """
        pass

    __state__ = abstractproperty()
    
# Thus it would be
def instancecheck(obj, cls):
    return subclasscheck(obj, TypeExpression(cls) & HasClass )
