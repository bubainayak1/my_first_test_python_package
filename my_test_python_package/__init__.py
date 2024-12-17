# my_test_python_package/__init__.py

from .module1 import concatenate, upper_case 
from .module2 import add, subtract
print("Initializing my_test_python_package")
from .subpackge import Test_module1, Test_module2  # Correct import
__all__ = ['add', 'subtract','concatenate', 'upper_case']

