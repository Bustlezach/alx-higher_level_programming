#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total_args = len(sys.argv) - 1

    for i in range(total_args):
        if (total_args == 0):
            print("{total_args} arguments.")
        elif (total_args == 1):
            print("{total_args} argument: \n {i + 1}: {sys.argv[i + 1]}")
        else:
            print("{total_args} arguments: \n {i + 1}: {sys.argv[i + 1]}")
