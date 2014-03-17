#!/usr/bin/env python
import argparse
import re
from pprint import pprint

#
# argument parsing using argparse
#
parser = argparse.ArgumentParser()
parser.add_argument('positional_args',
                    nargs='?',
                    metavar='ARG')
parser.add_argument('--file', '-f',
                    dest='file')
parser.add_argument('--verbose', '-v',
                    dest='verbose',
                    action='store_true')
args = parser.parse_args()
myfile = args.file
verbose = args.verbose

# if no file as option, first argument has to be the file
if myfile == None:
    myfile = args.positional_args

# The flags -h and --help and the usage message are generated automatically.
# Positional arguments are in args.positional_args
# Options can follow positional arguments.
## print args


#
# 3D point class
#

class Point3D(object):
    """3D Point class with public x,y,z attributes """
 
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def list(self):
        """ Returns a list of XYX values"""
        return [self.x, self.y, self.z]

class Node(Point3D):
    """Graph node point class in 3D space """
 
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

        
class Segment(object):
    """List of points """
 
    def __init__(self, start, end, count, points, diameter):
        self.start = start
        self.end = end
        self.count = count
        self.points = points
        self.diameter = diameter
                        
class Skeleton(object):
    """nodes, segments, and their locations """
 
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y


#
# main
#


nodes = []

#print "Hello"
counter = 0

try:
    f = open(myfile)
except (TypeError, IOError):
    print "File not given or does not exist: ", myfile
    exit(1)
    
for line in f:
    # trim white space, including \r,\n
    line = line.strip()
    # ignore empty lines
    if not line:
        continue

    # skip intro
    header = re.search('^@', line)
    if counter == 0 and not header:
        continue
    # header
    if header:
        counter+= 1
        continue

    if counter == 1:
        match = re.search('([\d\.e\+\-]+) ([\d\.e\+\-]+) ([\d\.e\+\-]+)', line)
        x,y,z = match.groups()
        p = Point3D(x,y,z)
        nodes.append(p)
        
    print(line)
    


pprint(nodes)
pprint(nodes[0].__dict__)
