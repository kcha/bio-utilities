#!/usr/bin/python

# (c) 8/31/2009, Kevin Ha, McGill University
#
# Filename: Generate random reads for testing purposes
import sys
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
import random
from optparse import OptionParser

READ_LEN = 50
NUM_READS = 200

###############################################################################
usage = "usage: python %prog [options] reference.fa"
parser = OptionParser(usage=usage)
parser.add_option("-l", "--read-length", dest="read_len", default=READ_LEN,
                    metavar="INT", type="int",
                    help="Read length. [%default]")
parser.add_option("-n", "--num-reads", dest="num_reads", default=NUM_READS,
                    metavar="INT", type="int",
                    help="Number of reads to generate. [%default]")
(options, args) = parser.parse_args()
if len(args) == 0:
    parser.print_help()
    sys.exit()
###############################################################################

input_handle = open(args[0], 'r')

# go through each sequence record
for seq_record in SeqIO.parse(input_handle, "fasta"):
    len = len(seq_record)

    read_count = 0

    seq_obj = seq_record.seq

    for i in range(1,options.num_reads+1):
        read_count = read_count + 1

        # get start and end coordinates of new read
        end = random.randint(options.read_len, len)
        start = end - options.read_len

        # get read sequence
        new_read_string = seq_obj[start:end]
        #print new_read_string + "\t" + str(start) + "\t" + str(end)

        # create new read id
        new_read_id = seq_record.id + "_" + str(read_count) + "_" + str(start) + "_" + str(end)

        # create new SeqRecord
        new_seq_record = SeqRecord(Seq(str(new_read_string), IUPAC.unambiguous_dna), \
            id=new_read_id, description="")

        SeqIO.write([new_seq_record], sys.stdout, "fasta")

        

