# Basic Data Types
x = 5  # int object
y = 3.14  # float object
z = "Hello, World!"  # str object
a = True  # bool object

# Printing types of basic data types
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'str'>
print(type(a))  # Output: <class 'bool'>

# Complex Data Types
my_list = [1, 2, 3]  # list object
my_tuple = (1, 2, 3)  # tuple object
my_dict = {'a': 1, 'b': 2}  # dict object
my_set = {1, 2, 3}  # set object

# Printing types of complex data types
print(type(my_list))  # Output: <class 'list'>
print(type(my_tuple))  # Output: <class 'tuple'>
print(type(my_dict))  # Output: <class 'dict'>
print(type(my_set))  # Output: <class 'set'>

# Functions as Objects
def my_function():
    return "Hello from function"

# Printing type of function
print(type(my_function))  # Output: <class 'function'>

# Classes and Instances as Objects
class MyClass:
    def greet(self):
        return "Hello from MyClass"

# Printing type of class
print(type(MyClass))  # Output: <class 'type'>

# Creating an instance of MyClass
my_instance = MyClass()

# Printing type of instance
print(type(my_instance))  # Output: <class '__main__.MyClass'>

# Using a method from MyClass instance
print(my_instance.greet())  # Output: Hello from MyClass

# Modules as Objects
import math

# Printing type of module
print(type(math))  # Output: <class 'module'>

# Using an attribute from math module
print(math.sqrt(16))  # Output: 4.0

# Attributes and Methods of Objects
# Integer object method
print(x.bit_length())  # bit_length() is a method of int class

# String object method
print(z.upper())  # upper() is a method of str class

# Dynamic Typing Example
variable = 10  # int object
print(type(variable))  # Output: <class 'int'>

variable = "Now I'm a string"  # str object
print(type(variable))  # Output: <class 'str'>
