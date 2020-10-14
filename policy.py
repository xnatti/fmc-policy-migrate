#!/usr/bin/env python3
import json



print('filename: ', end='')
filename = input()

stuffs = {}


def readPolicy(filename):
    placeholder = {}
    with open (filename) as file:
        placeholder = json.load(file)
    return placeholder



policy = readPolicy(filename)


def extractZones(policy):
    zoneset = set()
    for item in policy['items']:
        if 'sourceZones' in item:
            for zone in item['sourceZones']['objects']:
                zoneset.add(zone['name'])
        if 'destinationZones' in item:
            for zone in item['destinationZones']['objects']:
                zoneset.add(zone['name'])
    return zoneset


stuffs['zones'] = extractZones(policy)


def extractPortObjects(policy)
    objectset = set()
    for item in policy['items']:
        if 'destinationPorts' in item:
            if 'objects' in item['destinationPorts']:
                for obj in item['destinationPorts']['objects']:
                    objectset.add(obj['name'...........................waitthisisnotIT!!!

