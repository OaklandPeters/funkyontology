"""
Example abstract interfaces for namespace and chained namespaces.

To make chained namespace support multiple inheritance, this will
have to handle the linearized C3 algorithm, which Python uses.

Note: careful analogy/equivalence between Logicals and Sets

Difficult question:
    A = Namespace(...)
    B = Namespace(...)
    C = A | B  # intersection
    assert isinstance(C, ChainedNamespace)  # yes or no?


Advanced functions
======================
abstract_extension(klass, interface):


"""


from abc import ABCMeta, abstractproperty, abstractmethod

from logical import SetLogical, SetNesting



class NamespaceInterface(Mapping, SetLogical):
    """
    This is for a non-mutable namespace

    This should implement functionality of:
        Mapping
        ~ Logical (basically... booleans)
    """
    __metaclass__ = ABCMeta



    @abstractmethod
    def __contains__(self, value):
        pass
    def has(self, other):
        return self.__contains__(other)

    @abstractmethod
    def __getitem__(self, key):
        pass
    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError, AttributeError:
            return default

    # ------  Mapping functions
    @abstractmethod
    def items(self):
        pass

    @abstractmethod
    def keys(self):
        """
        ~ dir()
        """
        pass

    @abstractmethod
    def values(self):
        pass


class ChainedNamespaceInterface(NamespaceInterface, SetNesting):
    """
    This sort of behavior is most frequently used for:
    (1) multi-layered configuraiton overrides
    (2) Emulating stack/scope of variables
    (3) Commandline path searches (~stack of directories)
    (4) Django's `Context` class

    Other benefits, lets you ask:
        Am I getting the "default value?
        What is the original/"default" value?
        At what level did the default get overridden? (eg user-specified or command-line overrides?)

    Speed tradeoffs:
        Given N layers, and at most M keys in each layer
        Chainmap: construction is O(N) and key lookup is O(M)
        dict: construction is O(N*M) and key lookup is O(1) - O(M) worst case


    Programming details:
    ChainedNamespaces act like Sets, while simpler Namespaces do not.
    This is because ChainedNamespaces have the concept of inheritance/tree.


    This class should implement the same functionality as:
        collections.Set
        collections.ChainMap

    """
    # Implied by SetNesting:
    #   issubset
    #   issuperset
    @abstractmethod
    def issubset(self, other):
        pass


    def meets(self, interface):
        """
        Ask if this satisfies an interface, ~has the same methods/method-signatures
        """

    def flatten(self):
        """
        ~ vars(), *Internal* namespace
        Returns a Namespace (not chained)
        """

