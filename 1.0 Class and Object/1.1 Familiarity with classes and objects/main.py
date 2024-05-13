# Description of the class
class MyClass:
    pass

#Create a object
A=MyClass()
B=MyClass()

# Objects
print("A:", A)
print("B:", B)

# Type of the objects
print("A:", type(A).__name__)
print("B:", type(B).__name__)

# Compare
print("A == B", A == B)

# Result
"""
A: <__main__.MyClass object at 0x0000019A4F2D59A0>
B: <__main__.MyClass object at 0x0000019A4F2D5940>
A: MyClass
B: MyClass
A == B False
"""