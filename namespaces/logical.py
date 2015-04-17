"""
Defines a logical, a kind of base class for boolean like values.

This is used by Namespace


In Python sets, the non-operator versions of union(), intersection(), difference(), and symmetric_difference() will accept any iterable as an argument. In contrast, their operator based counterparts require their arguments to be sets. This precludes error-prone constructions like Set('abc') & 'cbs' in favor of the more readable Set('abc').intersection('cbs').

"""
from abc import ABCMeta, abstractmethod

class SetLogical(object):
    """ Supporting class.
    Logical/boolean-like operations, which make sense on sets (or Namespaces).

    These construct new objects

    Note, for sets, most operations are non-commutative.

    Difficult decision: which to support
        myset = Logical(...)
        ~myset            # unary inversion
        myset - otherset  # binary inversion

        The Reason: over sets, inversion is not defined
    """
    @abstractmethod
    def union(self, other):
        pass

    @abstractmethod
    def intersection(self, other):
        pass

    @abstractmethod
    def difference(self, other):
        pass

    def symmetric_difference(self, other):
        _union = self.union(other)
        _intersection = self.intersection(other)
        return _union.difference(_intersection)

    # Operator versions
    def __or__(self, other):
        return self.union(other)

    def __and__(self, other):
        return self.intersection(other)

    def __sub__(self, other):
        return self.difference(other)

    def __xor__(self, other):
        return self.symmetric_difference(self, other)




class SetNesting(object):
    """
    These ask questions
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def issubset(self, other):
        pass

    @abstractmethod
    def issuperset(self, other):
        pass

    # Operator versions
    def __le__(self, other):
        return self.issubset(other)

    def __ge__(self, other):
        return self.issuperset(other)
