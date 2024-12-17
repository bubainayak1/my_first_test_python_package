To create a directory in Windows using the command line, you can use the mkdir command (short for "make directory").
Steps:
Open Command Prompt:
Press Windows + R, type cmd, and press Enter to open the Command Prompt.
Create a Directory:
Use the mkdir command followed by the name of the directory you want to create.
Example:
To create a directory named new_folder in the current directory:
bash
Copy code
mkdir new_folder

This will create a folder named new_folder in your current directory.
Creating a Directory in a Specific Path:
If you want to create the directory in a specific location, provide the full path. For example, to create a folder my_project in the C:\Users\YourUsername\Documents directory:
bash
Copy code
mkdir C:\Users\YourUsername\Documents\my_project

Creating Multiple Directories at Once:
You can also create multiple directories at once by specifying them all after the mkdir command:
bash
Copy code
mkdir folder1 folder2 folder3

This will create three directories named folder1, folder2, and folder3 in the current directory.
Conclusion:
The mkdir command in Windows allows you to quickly create directories from the command line, either in the current directory or a specific location by providing the full path.


To create a file in Windows using the command line,
 you can use different commands depending on the type of file you want to create. Below are a few common ways to create files in Windows:
1. Using echo Command (for Text Files):
The echo command is used to create a file and write text into it.
Example: Create a text file example.txt with some content:
bash
Copy code
echo This is a new file > example.txt

This will create a file named example.txt in the current directory with the text "This is a new file".
If you want to append text to the file (if it already exists):
bash
Copy code
echo Additional text >> example.txt

2. Using type nul Command (Empty Files):
The type nul command creates an empty file.
Example: Create an empty text file emptyfile.txt:
bash
Copy code
type nul > emptyfile.txt



Package:

In Python, a package is a collection of modules organized in directories, allowing you to structure your code in a hierarchical manner. A package can contain multiple modules, sub-packages, and other resources, such as documentation or data files, and it provides a way to organize and reuse code more effectively.
Key Points About Python Packages:
Modules are individual Python files (.py), which can contain functions, classes, and variables.
Packages are directories that contain multiple modules and must include a special file called __init__.py to be recognized as a package. This file can be empty or contain initialization code for the package.



1. Directory Structure look like 
Create the following structure for your package:

my_test_python_package/
│
├── my_test_python_package/
│   ├── __init__.py                # Initialize main package
│   ├── module1.py                 # A module in the main package
│   ├── module2.py                 # Another module in the main package
│   ├── subpackage/                # Subpackage directory
│   │   ├── __init__.py            # Initialize the subpackage
│   │   ├── Test_module1.py        # Module in the subpackage
│   │   └── Test_module2.py        # Another module in the subpackage
│
├── setup.py                       # For packaging (optional but recommended)
└── README.md                      # Documentation (optional)


2. Code for Package Modules
my_test_python_package/__init__.py
This file initializes the main package and exposes selected modules or functions.
# my_test_python_package/__init__.py

from .module1 import concatenate, upper_case 
from .module2 import add, subtract
from .subpackge import Test_module1, Test_module2  # Correct import

print("Initializing my_test_python_package")
__all__ = ['add', 'subtract','concatenate', 'upper_case']


my_test_python_package/module1.py

def concatenate(str1, str2):
    return str1 + str2

def upper_case(text):
    return text.upper()


my_test_python_package/module2.py

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y


my_test_python_package/subpackage/__init__.py
This file initializes the subpackage and exposes its modules.
# subpackage/__init__.py

from .Test_module1 import Test_module1
from .Test_module2 import Test_module2

print("Initializing from subpackge")
__all__ = ['Test_module1', 'Test_module2']




# my_test_python_package/subpackage/Test_module1.py

class Test_module1:
    def __init__(self):
        self.name = "Test Module 1"
    
    def test(self):
        return "Test method from Test_module1"


# my_test_python_package/subpackage/Test_module2.py

class Test_module2:
    def __init__(self):
        self.name = "Test Module 2"
    
    def test(self):
        return "Test method from Test_module2"



Test package: from same directory 👍
1.

import my_test_python_package as package
#from package import Test_module
# In the main package `__init__.py` or any other module
print("Package attributes:")
print(dir(package))

2.# Print all modules, classes, and functions in the package


import my_test_python_package as package
import inspect


print("Package Details:")
for name, obj in inspect.getmembers(package):
    if inspect.isfunction(obj):
        print(f"Function: {name}")
    elif inspect.isclass(obj):
        print(f"Class: {name}")
    elif inspect.ismodule(obj):
        print(f"Module: {name}")

3.
import my_test_python_package as package
from my_test_python_package import subpackge


# Print main package attributes
print("Main Package Attributes:")
print(dir(package))


# Print subpackage attributes
print("\nSubpackage Attributes:")
print(dir(subpackge))



#4. List All Files Inside the Package

import os
import my_test_python_package


# Path to the package
package_path = os.path.dirname(my_test_python_package.__file__)


# Walk through the package directory and print files
print("Package File Structure:")
for root, dirs, files in os.walk(package_path):
    print(f"Directory: {root}")
    for file in files:
        print(f"  File: {file}")






5.# Print package help and details
import my_test_python_package as package


# Print package help and details
help(package)


Here details example  how call and import package and subpackage 👍

from my_test_python_package.subpackge.Test_module1 import Test_module1
from my_test_python_package.subpackge.Test_module2 import Test_module2
import my_test_python_package as package




#Use the alias 'package' to access the functions
result_add = package.add(5, 3)
result_subtract = package.subtract(10, 4)
result_concat = package.concatenate("Hello", " World")
result_upper = package.upper_case("hello")






print(result_add)       # Output: 8
print(result_subtract)  # Output: 6
print(result_concat)    # Output: Hello World
print(result_upper)     # Output: HELLO






submodule1=Test_module1()
print(submodule1.test())


submodule2=Test_module2()
print(submodule2.test())



Setup or install this package locally we need to write setup.py  that directory look like below :

my_test_python_package/
│
├── my_test_python_package/
│   ├── __init__.py                # Initializes main package
│   ├── module1.py                 # Module 1 in the main package
│   ├── module2.py                 # Module 2 in the main package
│   └── subpackage/                # Subpackage directory
│       ├── __init__.py            # Initializes the subpackage
│       ├── Test_module1.py        # Test module 1 in subpackage
│       └── Test_module2.py        # Test module 2 in subpackage
│
├── setup.py                       # For packaging
└── README.md                      # Optional, for documentation



2. Create the setup.py File
The setup.py file is used to configure and install your package. Place it at the root level of the directory (outside the my_test_python_package folder).
Here’s the code:
from setuptools import setup, find_packages


setup(
    name="my_test_python_package",    # Package name
    version="0.1",                    # Version number
    description="A test package with subpackages",  # Short description
    author="Your Name",               # Author name
    author_email="your.email@example.com",  # Author email
    url="https://example.com",        # Project URL (optional)
    packages=find_packages(),         # Automatically includes all packages and subpackages
    include_package_data=True,        # Include non-code files (optional)
    install_requires=[],              # Add dependencies here if needed
    classifiers=[                     # Metadata for PyPI (optional but recommended)
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',          # Specify the Python version
)


3. Install the Package Locally
Follow these steps to install and test your package locally:
a. Open a terminal or command prompt:
Navigate to the folder containing setup.py:

cd path/to/my_test_python_package

b. Install the package in editable mode:
Run the following command:
pip install -e . or pip install .

The -e flag means "editable mode," so you can modify the source code without reinstalling the package.
c. Verify the Installation:
Run this command to confirm that the package is installed:

pip show my_test_python_package

You should see the package details, including the location of the installation.

Local install vs build process:
Local Installation
The local installation allows you to use your package on your machine as if it were globally installed. You can test it before distributing it.
Why Install Locally?
To test your package in a real-world scenario.
To validate dependencies and functionality.
To use the package in other projects or scripts.
Types of Local Installation:
Editable Install (-e):
Links your package directory directly to your Python environment.
Changes made to your code are reflected without reinstalling.
Command:

pip install -e .


Non-editable Install:
Installs the package like a standard package from PyPI.
Command:

pip install dist/my_test_python_package-0.1-py3-none-any.whl


Use of Local Installation:
Speeds up development and testing.
Helps you test the behavior as if your package were used by others.
Ensures the setup.py and dependencies are correctly handled.



Build Process: Packages your code for portability, sharing, and distribution.
Old process 

my_test_python_package/
│
├── my_test_python_package/
│   ├── __init__.py
│   ├── module1.py
│   ├── module2.py
│   ├── subpackage/
│       ├── __init__.py
│       ├── Test_module1.py
│       ├── Test_module2.py
│
├── setup.py
├── README.md
Step 2: Install Build Tools
Make sure you have the required tools installed. Run this command:
pip install --upgrade setuptools wheel
setuptools: Handles the packaging process.
wheel: Builds the package into a wheel format (.whl).


Step 3: Build the Package
In your package's root directory (where setup.py is located), run the following command:
python setup.py sdist bdist_wheel

What happens here?
sdist: Creates a source distribution (a .tar.gz file).
bdist_wheel: Builds a wheel distribution (a .whl file) for faster installation.
Step 4: Check the Build Output
After running the build command, a dist/ folder will be created. It will contain:
dist/
│
├── my_test_python_package-0.1.tar.gz   # Source distribution
├── my_test_python_package-0.1-py3-none-any.whl  # Wheel distribution
.tar.gz: A compressed archive of the source code.
.whl: A pre-built wheel file, faster to install.
Step 5: Install the Built Package Locally
To test your built package locally, run:
pip install dist/my_test_python_package-0.1-py3-none-any.whl

Copy code
pip install dist/my_test_python_package-0.1.tar.gz





New build process also using   project.toml  please check new approach 
