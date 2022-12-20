#!/usr/bin/python3
def uniq_add(my_list=[]):
<<<<<<< HEAD
    new = set(my_list)
    res = 0
    for i in new:
        res += i
    return res
=======
    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

    return (num)
>>>>>>> 6aba5d5 (corrections)
