#!/usr/bin/python3
def search_replace(my_list, search, replace):
<<<<<<< HEAD
    copy = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            copy.append(replace)
        else:
            copy.append(my_list[i])
    return copy
=======
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
>>>>>>> 6aba5d5 (corrections)
