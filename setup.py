from setuptools import setup, find_packages

setup(
    name="my_test_python_package",    # Package name
    version="0.1",                    # Package version
    description="A test package with subpackages",  # Short description
    author="Soumen Nayak",            # Your name
    author_email="your.email@example.com",  # Your email
    url="https://example.com",        # URL for the package/project
    packages=find_packages(),         # Automatically find packages and subpackages
	install_requires=[],              #A list of required third-party packages (dependencies). These will be automatically installed when the package is installed.
    python_requires='>=3.7.3',        # Supported Python version
)
