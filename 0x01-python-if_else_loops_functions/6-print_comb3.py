#!/usr/bin/python3
for i in range(100):
    if i < 99 and i % 10 > i / 10:
        print("{:02d}, ".format(i), end='')
    if i == 89:
        print("{:02d}".format(i))
