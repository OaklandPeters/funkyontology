"""
Morhpisms are functions defined within TypeExpression
(from a TypeExpression to a TypeExpression)


Query: (similarity to algebraic rings)
    Is there an identity element for the category of TypeExpressions?
    That is, some element: IdExpr, such that
        union(expr in TypeExpression, IdExpr) == expr
        intersection(expr, IdExpr) == expr

    ... for intersection, this would just be an empty expression ({})
    ... for union, this would AnyType:
        Union(expr, AnyType) == expr

"""

def union(left, right):
    """
    union(TypeExpression, TypeExpression) -> TypeExpression

    Commutative
        A | B == B | A
    Variadic, and associative
        union(A, B, C) == union(union(A, B), C)
        A | (B | C) == (A | B) | C == |(A, B, C)

    Union(TypeExpression, )
    """
union.identity = EmptyType

def intersection(left, *rights):
    """
    ~multiple inheritance
    Not commutative
        intersection(A, B) != intersection(B, A)
        A & B       !=      B & A
    Variadic and not associative
        intersection(A, intersection(B, C)) != intersection(A, B, C)
        A & (B & C)     !=      &(A, B, C)

    intersection(TypeExpression, Sequence[TypeExpression]) -> TypeExpression
    """
intersection.identity = AnyType




def difference(left, right):
    """
    Not commutative

    difference(TypeExpression, Sequence[TypeExpression]) -> TypeExpression
    """
difference.identity = EmptyType

def symmetric_difference(left, right):
    """
    ~unique elements
    Commutative
        A ^ B == B ^ A
    Variadic and associative
        A ^ (B ^ C) == 

    """
symmetric_difference.identity = 
