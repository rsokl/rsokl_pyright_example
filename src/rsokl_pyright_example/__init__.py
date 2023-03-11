from typing_extensions import NewType
print("Using typing_extensions")

__all__ = ["Apple"]

Apple = NewType("Apple", int)
