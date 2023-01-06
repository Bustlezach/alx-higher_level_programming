#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    no_of_args = len(sys.argv) - 1

    total_args = 0
    for i in range(no_of_args):
        total_args += int((sys.argv[i + 1]))
    print(f"{total_args}")
