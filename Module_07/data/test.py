import os
import sys

fh = open(sys.argv[1], "r")

for line in fh:
    test_line = line.split(" ")
    with open("messlog", "a") as fl:
        test = ",".join(test_line)
        fl.write(test)
