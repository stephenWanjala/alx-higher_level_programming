#!/usr/bin/python3
<<<<<<< HEAD
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
=======

def magic_calculation(a, b):
    """Match bytecode provided"""
    from magic_calculation_102 import add, sub

>>>>>>> 6aba5d5 (corrections)
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
<<<<<<< HEAD
        return c
    else:
        return sub(a, b)
=======
        return (c)

    else:
        return (sub(a, b))
>>>>>>> 6aba5d5 (corrections)
