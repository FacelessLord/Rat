from abc import abstractmethod
from typing import List, Optional

from contexts.types import ContextType
from tree.builder import TreeBuilder
from tree.node import TreeNode


class Context:
    position_filled = False
    children: List["Context"] = None
    parent: Optional["Context"] = None
    ref: int = -1
    track_commas = False

    def __init__(self):
        self.children = []

    def collect(self, ctx: "Context"):
        if self.position_filled and self.track_commas:
            raise ValueError(f"Lost comma when collecting {ctx}")
        self.position_filled = True
        ctx.parent = self
        ctx.ref = len(self.children)
        self.children.append(ctx)

    def wrap_with(self, ctx: "Context"):
        self.parent.children[self.ref] = ctx
        ctx.parent = self.parent
        ctx.collect(self)

    def set_position_empty(self, ignore_empty: bool = False):
        if not self.position_filled and not ignore_empty and self.track_commas:
            raise ValueError("Two commas together")
        self.position_filled = False

    @staticmethod
    def get_type() -> ContextType:
        pass

    @abstractmethod
    def to_tree_node(self, builder:TreeBuilder) -> TreeNode:
        pass

    def __repr__(self):
        return f"{self.get_type()}{self.children}"
