#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    sum_args = 0
    for i in range(1, count):
        sum_args += int(sys.argv[i])
    print("{}".format(sum_args))
