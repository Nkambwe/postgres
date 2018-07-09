"""
postgres/project/util.py
"""

def greet(name):
    """
    name: user name which must be a string type
    """
    if type(name) != str:
        raise TypeError("Argument must be s string type")

    if name.strip() == "":
        raise ValueError("argument cannot be empty")
        
    print('Hello {}'.format(name))