# subpackge/__init__.py

from .Test_module1 import Test_module1
from .Test_module2 import Test_module2

print("Initializing from subpackge")
__all__ = ['Test_module1', 'Test_module2']

