#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
<<<<<<< HEAD
    for i in sorted(a_dictionary):
        print("{:s}: {}".format(i, a_dictionary[i]))
=======
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for i in list_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
>>>>>>> 6aba5d5 (corrections)
