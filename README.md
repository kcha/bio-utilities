bio-utilities
==============

My collection of bioinformatics-related utility scripts

Installation
------------
    make install

This just copies scripts from src/ folder to bin/.

Utilities
---------
 * `bitwise_flag` - Describe bitwise FLAG from SAM file
 * `create_random_reads` - Naively generate random read sequences from a
 reference FASTA file (requires Biopython)
 * `find_in_bed` - Find intervals in a BED file given chr, start, and end

Unit tests
----------
    make test
