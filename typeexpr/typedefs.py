"""

Concrete types (~inherited from):

    TypeType
    InstanceType
    ShallowNamespace
    ChainedNamespace
    TypeExpression


Abstract types (~not inherited from):
    Abstract
    HasState
"""
import types

from ..namespaces import namespace
from . import hasstate

__all__ = [
    
]

TypeType = types.TypeType
InstanceType = object
ShallowNamespace = namespace.ShallowNamespace
ChainedNamespace = namespace.ChainedNamespace
HasState = hasstate.HasState

# Define class Abstract here
