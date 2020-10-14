#!/usr/bin/env python3
import json



print('filename: ', end='')
filename = input()



def readPolicy(filename):
    placeholder = {}
    with open (filename) as file:
        placeholder = json.load(file)
    return placeholder



policy = readPolicy(filename)
