#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
<<<<<<< HEAD
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
=======
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return (a_dictionary)
>>>>>>> 6aba5d5 (corrections)
