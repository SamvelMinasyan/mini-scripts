# shadowing_builtin.py

def list():  # Shadowing the built-in function 'list'
    return [1, 2, 3]

print(list())
