#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_args = len(sys.argv) - 1
    if n_args == 0:
        print("{}".format(0))
    else:
        i = 0
        result = 0
        for a in sys.argv:
            if i != 0:
                result += int(a)
            i += 1
        print("{}".format(result))
