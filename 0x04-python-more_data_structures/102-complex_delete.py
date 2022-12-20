#!/usr/bin/python3
def complex_delete(a_dictionary, value):
<<<<<<< HEAD
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
=======
    list_keys = list(a_dictionary.keys())

    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return (a_dictionary)
>>>>>>> 6aba5d5 (corrections)
