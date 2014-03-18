#!/usr/bin/env python
import argparse
import re
from pprint import pprint


#
# Node class
#

class Node(object):
    """Graph node point class in 3D space """

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

#
# 3D point class
#

class Point3D(Node):
    """3D Point class with public x,y,z attributes and optional set of diameters """

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

        self.diameters = []

    def list(self):
        """ Returns a list of XYX values"""
        return [self.x, self.y, self.z]

    def add_diameter(self, dia):
        self.diameters.append(dia)


#
# Segment class
#

class Segment(object):
    """List of points """

    def __init__(self, start, end):
        self.start = start
        self.end = end

        self.pointcount = None
        self.points = []

    def __len__(self):
        self.pointcount

#
# Skeleton class
#

class Skeleton(object):
    """Top storage object for a skeleton that knows about
    nodes, segments, and their locations """

    def __init__(self):
        self.nodes = {}
        self.segments = []

    def add_node(self, name, node):
        self.nodes.setdefault(name, node)

    def add_segment(self, segment):
        #self.nodes.setdefault(name, node)
        self.segments.append(segment)

    def add_points(self, points):
        c = 0
        point_count = 0
        seg_count = self.segments[c].pointcount
        for point in points:
            point_count += 1;
            s = self.segments[c]
            if point_count == seg_count:
                c =+ 1
                seg_count += self.segments[c].pointcount
            self.segments[c].points.append(point)

    def info(self):
        print "Nodes    : " + str(len(self.nodes))
        print "Segments : " + str(len(self.segments))
        c = 0
        for s in self.segments:
             c+= len(s.points)
        print "Points   : " + str(c)

#
# AmirameshReader class
#

class AmirameshReader(object):
    """ Read from a filehandle, parse, return a Skeleton object"""

    def parse(self, f):

        skel = Skeleton()       # storage object
        points = []             # list of points
        counter = 0             # section counter
        linecounter = 0         # within sections

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

            if counter == 1:            # nodes
                match = re.search('([\d\.e\+\-]+) ([\d\.e\+\-]+) ([\d\.e\+\-]+)', line)
                x,y,z = match.groups()
                x = float(x)
                y = float(y)
                z = float(z)
                n = Node(x,y,z)
                skel.add_node(linecounter,n)
                linecounter += 1

            elif counter == 2:          # segments to nodes
                match = re.search('(\d+) (\d+)', line)
                start,end = match.groups()
                seg = Segment(start, end)
                #print type(skel), type(skel.add_segment)
                skel.add_segment(seg)

            elif counter == 3:          # point count within segment
                match = re.search('(\d+)', line)
                count = match.groups()
                skel.segments[linecounter].pointcount = count
                linecounter += 1

            elif counter == 4:          # point coordinates within a segment
                match = re.search('([\d\.e\+\-]+) ([\d\.e\+\-]+) ([\d\.e\+\-]+)', line)
                x,y,z = match.groups()
                x = float(x)
                y = float(y)
                z = float(z)
                p = Point3D(x,y,z)
                #skel.add_point(linecounter, p)
                points.append(p)
                #linecounter += 1

            elif counter > 4:           # one or more diameters
                # empty values replaced by 0
                if line == "nan":
                    line = "0.0"

                match = re.search('([\d\.e\+\-]+)', line)
                dia = match.groups()[0]
                dia = float(dia)
                points[linecounter].add_diameter(dia)
                linecounter += 1

        # add points in the end for efficiency
        skel.add_points(points)
        return skel

#
# main
#

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


try:
    f = open(myfile)
except (TypeError, IOError):
    print "File not given or does not exist: ", myfile
    exit(1)

reader = AmirameshReader()
skel = reader.parse(f)

if verbose:
    skel.info()

#
# end of main
#

# debugging

#pprint(skel.__dict__)
#pprint(skel.segments[0].__dict__)
#pprint(skel.segments[0].points[0].__dict__)
