#!/usr/bin/python3
import sys

# Check if arguments are passed, excluding the script name
if len(sys.argv) > 1:
    print("Arguments passed to the script:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")
else:
    print("No additional arguments passed.")
