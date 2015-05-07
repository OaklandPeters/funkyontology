"""
Functors defined on TypeExpression
(functions from a TypeExpression to another type)


instancecheck(Any, TypeExpression) -> Boolean
subclasscheck(TypeExpression, TypeExpression) -> Boolean
meets(TypeExpression, AbstractTypeExpression) -> Boolean
hasattr(TypeExpression, str) -> Boolean
getattr(TypeExpression, str) -> Any
flatten(TypeExpression) -> ShallowNamespace
terms(TypeExpression) -> Iterator[(str, Any)]
construct(TypeExpression, Optional[ShallowNamespace]) -> TypeType


"""

def instancecheck(obj, typeexpr):
    """
    instancecheck(Any, TypeExpression) -> Boolean
    """
    # eventually, this might simplify to:
    # return subclasscheck(obj, typeexpr & HasState)

def subclasscheck(obj, typeexpr):
    """
    subclasscheck(TypeExpression, TypeExpression) -> Boolean
    """

def getattr(typeexpr, name):
    """
    getattr(TypeExpression, str) -> Any
    """

def hasattr(typeexpr, name):
    """
    hasattr(TypeExpression, str) -> Boolean
    """

def flatten(typeexpr):
    """
    flatten(TypeExpression) -> ShallowNamespace
    ~ this is basically 'vars()'
    """

def terms(typeexpr):
    """
    terms(TypeExpression) -> Iterator[(str, Any)]

    Basically, an iterator over the attributes in this typeexpression.
    Conceptually similar to: namespace.keys()
    """


def meets(typeexpr, abstractexpr):
    """
    meets(TypeExpression, AbstractTypeExpression) -> Boolean

    Related function:
    def matches(attribute, signature):
        # matches(Any, Signature) -> Boolean
    def matches(attribute, other):
        # matches(Any, Any) -> Boolean
        # matches(attribute, get_signature(Any)) -> Boolean
        # ... extracts the signature of 2nd argument
    def get_signature(Any) -> Signature
    """
    # this may simplifiy to (if Abstract is just any typeexp, 
    #       and may have some methods who are abstract)
    # meets(TypeExpression, TypeExpression) -> Boolean


def construct(typeexpr, namespace={}):
    """
    construct(TypeExpression, Optional[ShallowNamespace]) -> TypeType
    
    ~ class constructor
    ~ Python's type(name='', bases=typeexpr, dict=namespace)

    Related:
        setattr(FlatNamespace, str, Any) -> FlatNamespace
        delattr(FlatNamespace, str) -> FlatNamespace

        ... ACTUALLY: these are meaningful on a FlatNamespace, or an instance (~ HasState)
    """
    shallow = ShallowNamespace(namespace)
    chained = ChainedNamespace(typeexpr, shallow)
    cls = stuff # ... some other magic
    return cls

def convert(cls):
    """
    Converts a class into a typeexpression.
    ~ returns it's mro

    def convert(TypeType) -> TypeExpression
    def convert()
    """

convert(TypeType) -> TypeExpression
    # this is the constructor



