Logical Ontology: The Necessary Parts
========================================
These are operations (~functions) that the ontology should be able to preform.

Categorical Containment
-------------------------
: Subset (|)
- Inheritance Lattice
- Concrete multiple inheritance
- Established at object definition

Abstract Containment
----------------------
: Implies (->)
- Interfaces
- May also include `Virtual Containment` (virtual subclassing)
- Calculated (not read directly from method resolution order)

Ordered Intersection
---------------------
- Non-commutative (A & B =/= B & A)
- ~ base classes in multiple inheritance
- Combines traits/attributes of multiple types.
- Must be ordered because attributes of one may overwrite attributes of another

Unordered Intersection
-----------------------
: Symmetric Intersection (^)
- Commutative (A ^ B == B ^ A)
- ~ Mixins
- ~ Multiple inheritance without conflicts
- Can be made easier by having concept of private methods. IE public methods can access private methods of the class, but not the private methods of child classes)
- Useful for mixins/Traits
- Pythonically, it might be possible to implement, by wrapping all non-public methods is a decorator, which swaps out the class/self which is provided to that method
    - ... I have implemented somethign like this before as `abcview`

Type Union
--------------

Type Inversion
-----------------
- For concrete types, says "did not inherit"
- Used for excluding edge cases

Enumerated Types
------------------
- Specifies permissible values
- Often used to map values to symbols (ex. usa_states: str --> symbol)
- Useful for pattern matching

Maybe... Sequence Types
-------------------------
Related to enumerated types

Maybe... Type Restriction
--------------------------
- Restrict a concrete class down to those elements which match an abstract class


Algebraic Types
------------------
- Handles "Nesting"/"Of" situations
- Example:: Sequence[A'] : { __iter__: () --> { __next__: () --> A'}}
    - Translated, this means:
        iter(Sequence(A')) returns an Iterable object with a __next__ method, and the __next__ method returns type A'
- =/= Intersection/Union types
- Something like algebra over nested tree structures. Functional languages handle this, others do not.



For object oriented systems, at least, there are three ways that operations are used:
(1) Predicate. Asks if some relation holds between types.
    "Is type A a subset of type B"
(2) New type construction. Builds a new data structure of *all* methods and attributes of the new type.
(3) Since method retreival. For a constructed type - retreive it from the type expression.
