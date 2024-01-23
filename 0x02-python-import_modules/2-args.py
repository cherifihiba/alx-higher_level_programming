#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    # Calculate the number of arguments
    x = len(argv) - 1

    # Print the appropriate message based on the number of arguments
    if x == 0:
        print("0 arguments.")
    elif x == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(x))

    # Print the position and value of each argument
    for i in range(1, x + 1):
        print("{}: {}".format(i, argv[i]))
