#!/usr/bin/env python
"""
(c) 2010, Kevin Ha, McGill University

Parse a number taken from the bitwse FLAG in the SAM format and report the
results

Usage: python bitwise_flag.py SAM_flag
"""

import sys

flag = int(sys.argv[1])

#assert flag > 0, "Flag must be greater than zero!"
#if flag <= 0:
    #sys.stderr.write("Flag is 0 or less.\n")
    #sys.exit()

print "1\t0x1\tThe read is paired in sequencing:\t\t\t\t",
if (flag & 1): print "YES"
else: print "NO"

print "2\t0x2\tThe read is mapped in a proper pair:\t\t\t\t",
if (flag & 2): print "YES"
else: print "NO"

print "4\t0x4\tThe query sequence itself is unmapped:\t\t\t\t",
if (flag & 4): print "YES"
else: print "NO"

print "8\t0x8\tThe mate is unmapped:\t\t\t\t\t\t",
if (flag & 8): print "YES"
else: print "NO"

print "16\t0x10\tStrand of the query (0 for forward; 1 for reverse strand):\t",
if (flag & 16): print "REVERSE"
else: print "FORWARD"

print "32\t0x20\tStrand of the mate:\t\t\t\t\t\t",
if (flag & 32): print "REVERSE"
else: print "FORWARD"

print "64\t0x40\tThe read is the first read in a pair:\t\t\t\t",
if (flag & 64): print "YES"
else: print "NO"

print "128\t0x80\tThe read is the second read in a pair:\t\t\t\t",
if (flag & 128): print "YES"
else: print "NO"

print "256\t0x100\tThe alignment is not primary:\t\t\t\t\t",
if (flag & 256): print "YES"
else: print "NO"
print "\t\t(a read having split hits may have " \
"multiple primary \n\t\talignment records)"

print "512\t0x200\tThe read fails platform/vendor quality checks:\t\t\t",
if (flag & 512): print "YES"
else: print "NO"

print "1028\t0x400\tThe read is either a PCR duplicate or an optical duplicate:\t",
if (flag & 1028): print "YES"
else: print "NO"

print "2056\t0x800\tSupplementary alignment (e.g. chimeric alignment):\t\t",
if (flag & 2056): print "YES"
else: print "NO"
