#!/usr/bin/env python
import argparse
from pprint import pprint
from amiramesh import AmirameshReader

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
