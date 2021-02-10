from abc import abstractmethod
from typing import List

from contexts.types import ContextType
from sr_collections.variable_storage import VariableStorage


class TreeNode:
    children: List["TreeNode"] = None

    def __init__(self):
        self.children = []

    @abstractmethod
    def interpret(self, variable_storage: VariableStorage):
        pass

    @staticmethod
    def get_type():
        return ContextType.generic_context
