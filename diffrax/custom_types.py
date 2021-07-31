from dataclasses import dataclass
import jax  # noqa: F401  # has side effects: loads jaxlib.xla_extension
import jaxlib
from typing import Any, Optional, Tuple, Union


class Array:
    def __class_getitem__(cls, item):
        return Any


PyTree = Any

Scalar = Union[int, float, Array[()]]


# Not a tree_dataclass as we don't want to convert shapes, splits into jnp.arrays
@dataclass(frozen=True)
class SquashTreeDef:
    treedef: jaxlib.xla_extension.PyTreeDef
    shapes: Optional[Tuple[int]]
    splits: Optional[Tuple[int]]

    def __iter__(self):
        return iter((self.treedef, self.shapes, self.splits))
