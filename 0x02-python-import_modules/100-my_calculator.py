#!/usr/bin/python3

if __name__ == "__main__":
    """ Calc """
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    argc = len(argv)
    if (argc != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, ops[op](a, b)))
