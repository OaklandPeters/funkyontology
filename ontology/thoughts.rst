
Class VS Alias: in Ceylon
----------------------------
alias Num = Float|Integer
interface People => Set<Person>
(interfaces are same as classes in this regard)

You CAN inherit from interfaces and classes.
You can NOT inherit from aliases. Largely because union types do
not make sense as something to inherit from.



Usages of Type Operations
----------------------------
For object oriented systems, at least, there are three ways that operations are used:
(1) Predicate. Asks if some relation holds between types.
    "Is type A a subset of type B"
(2) New type construction. Builds a new data structure of *all* methods and attributes of the new type.
(3) Since method retreival. For a constructed type - retreive it from the type expression.
