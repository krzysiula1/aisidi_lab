import typing
from abc import ABC, abstractmethod
from typing import List

from typing_extensions import Protocol

C = typing.TypeVar("C", bound="Comparable")


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: C, other: C) -> bool:
        pass

    @abstractmethod
    def __gt__(self: C, other: C) -> bool:
        pass


class AbstractHeap(ABC):
    def __init__(self, num_children: int) -> None:
        pass

    def __len__(self) -> int:
        return len(self.get_raw_data())

    @abstractmethod
    def peek(self) -> C:
        """Get the topmost element without changing the heap."""

    @abstractmethod
    def push(self, value: C):
        """Add an element to the heap."""

    @abstractmethod
    def pop(self) -> C:
        """Remove the topmost element from the heap and return it."""

    @abstractmethod
    def get_raw_data(self) -> List[C]:
        """Get the underlying data storage."""
