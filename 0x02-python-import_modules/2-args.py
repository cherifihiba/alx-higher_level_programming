#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv) - 1
    if x < 1:
        print("{} arguments.".format(x))
    elif x == 1:
        print("{} argument:".format(x))
    else:
        print("{} arguments:".format(x))
    for i in range(x):
<<<<<<< HEAD
        print("{}: {:s}".format(i + 1, argv[i +1]))
=======
        print("{}: {:s}".format(i + 1, argv[i + 1]))
>>>>>>> fb9d5dea315056c1c6d5531c8da1fe3514152df8
