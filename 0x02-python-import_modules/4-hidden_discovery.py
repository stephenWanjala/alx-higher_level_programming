#!/usr/bin/python3

if __name__ == "__main__":
<<<<<<< HEAD
    from hidden_4 import *
    arr = dir()
    for i in range(0, len(arr)):
        if arr[i][0:2] != "__":
            print("{}".format(arr[i]))
=======
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
>>>>>>> 6aba5d5 (corrections)
