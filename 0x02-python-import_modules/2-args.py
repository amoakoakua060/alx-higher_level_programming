#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_args = len(sys.argv) - 1
    if n_args == 1:
        a = ""
    else:
        a = "s"
    if n_args == 0:
        b = "."
    else:
        b = ":"
    print("{} argument{}{}".format(n_args, a, b))
    if n_args != 0:
        for i in range(1, n_args + 1):
            print("{}: {}".format(i, sys.argv[i]))
