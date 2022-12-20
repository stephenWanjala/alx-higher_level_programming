#!/usr/bin/python3
def multiply_by_2(a_dictionary):
<<<<<<< HEAD
    new_d = {}
    for i in a_dictionary:
        new_d[i] = a_dictionary[i] * 2
    return new_d
=======
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for i in list_keys:
        new_dir[i] *= 2

    return (new_dir)
>>>>>>> 6aba5d5 (corrections)
