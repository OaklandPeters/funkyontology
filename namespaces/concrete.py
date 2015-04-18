"""
Concrete implementation of namespaces.

Advanced:
- Have union & intersection collapse repeated. Ex.
	A|B|C = (A|B)|C = NamespaceUnion(A, B)|C = NamespaceUnion(A, B, C)

"""
from namespace import ChainedNamespaceInterface, NamspaceInterface

class Namespace(NamespaceInterface):
	"""
	Namespace with no 'nesting', such as for purely local variables, or a
	'flattened' ChainedNamespace.
	"""

	def __init__(self, *args, **kwargs):
		self.data = dict(*args, **kwargs)

	@abstractmethod
    def union(self, *others):
        pass

    @abstractmethod
    def intersection(self, *others):
    	return ChainedNamespace(*others)

    @abstractmethod
    def difference(self, other):
        pass

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, value):
        return value in self.data
    # Alias
    def has(self, value):
        return self.__contains__(value)

    def __getitem__(self, key):
        return self.data.__getitem__(key)


class ChainedNamespace(ChainedNamespaceInterface):
	"""
	Concrete implemntation of a chained namespace
	"""

    @abstractmethod
    def issubset(self, other):
        pass

    @abstractmethod
    def issuperset(self, other):
        pass

    def __get__
    def flatten
    def items


class UnionNamespace(ChainedNamespaceInterface):
	def __init__(self, *namespaces):
		self.namespaces = namespaces

	def collapse(self, onto):
		assert onto in self.namespaces
		return onto

class IntersectionNamespace(ChainedNamespaceInterface):
	def __init__(self, *namespaces):
		self.namespaces = namespaces

class SubtractionNamespace(ChainedNamespaceInterface):
	pass

