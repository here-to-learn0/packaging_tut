# The usage of __init__.py file is it indicates that the files in this dir are part of python package. 
# Without an __init__.py file, you cannot import files from another directory in a Python project.

#__init__ can be empty but can also be used to set up imports. There are 3 kinds of imports:

# 1. example_package/__init__.py and explicit imports:

# from .example import sample_funciton 
# Where sample_function is the name of the function and .file1 is the name of the module/file

#Now in main.py I can direcly improt this function 


# 2.main_package/__init__.py and standard import:

# import example_package
# This imports the entire package

# 3. main_package/__init__.py and wild card import
# In __init__.py, set an __all__ variable to a list of the modules/files in the package.

# __all__ = ["file1", "file2", "file3"]
