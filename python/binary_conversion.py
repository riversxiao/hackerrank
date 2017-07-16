#!/bin/python3

import sys


n = int(input().strip())
t = "{0:b}".format(n)
print(max(map(len,t.split("0"))))
