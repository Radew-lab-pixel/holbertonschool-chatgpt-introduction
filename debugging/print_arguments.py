#!/usr/bin/python3
import sys

# Check if arguments are passed, excluding the script name
length = len(sys.argv)
if length > 1:
    # print("Arguments passed to the script:")
    for i in range(1, length, 1):
        print(sys.argv[i])
else:
    print("No additional arguments passed.")
