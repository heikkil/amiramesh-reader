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
#
# Node class
#

class Node(Point3D):
    """Graph node point class in 3D space """
 
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

#
# Segment class
#
        
class Segment(object):
    """List of points """
 
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = None
        self.points = None
        self.diameters = None
                        
#
# Skeleton class
#

class Skeleton(object):
    """nodes, segments, and their locations """
 
    def __init__(self):
        self.nodes = {}
        self.segments = []

    def add_node(self, name, node):
        self.nodes.setdefault(name, node)

    def add_segment(self, segment):
        self.segments.append(segment)
        

#
# main
#


nodes = []

#print "Hello"
counter = 0                     # sections
linecounter = 0                 # within sections

try:
    f = open(myfile)
except (TypeError, IOError):
    print "File not given or does not exist: ", myfile
    exit(1)

skel = Skeleton()                 # storage object
    
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
        linecounter = 0
        continue

    if counter == 1:
        match = re.search('([\d\.e\+\-]+) ([\d\.e\+\-]+) ([\d\.e\+\-]+)', line)
        x,y,z = match.groups()
        n = Node(x,y,z)
        skel.add_node("0",n)
        linecounter += 1

    elif counter == 2:
        match = re.search('(\d+) (\d+)', line)
        start,end = match.groups()
        seg = Segment(start, end)
        #print type(skel), type(skel.add_segment)
        skel.add_segment(seg)
        
    #elif counter == 3:
        
        
    print(line)
    


#pprint(nodes)
pprint(skel.__dict__)
