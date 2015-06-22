# Name: Samantha Prince
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
# gc_count = 0
# at_count = 0
a_count = 0
t_count = 0
c_count = 0
g_count = 0
n_count = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # if the bp is a C
    if bp == 'C':
        # increment the count of C
        c_count = c_count + 1
    # if the bp count is a G
    elif bp == 'G':
        # increment the count of G
        g_count = g_count + 1
    # if the bp is a G or a C,
    # elif bp == 'C' or bp == 'G':
        # increment the count of gc
        # gc_count = gc_count + 1
    # if bp is an A
    elif bp == 'A':
        # increment the count of A
        a_count = a_count + 1
    # if bp is T
    elif bp == 'T':
        # increment the count of T
        t_count = t_count + 1
    # if the bp is an A or T,
    # elif bp == 'A' or bp == 'T':
        # increment the count of gc
        # at_count = at_count + 1
    # if the bp is an N,
    elif bp == 'N':
        # increment the count of n
        n_count = n_count + 1


# divide the gc_count by the total_count
gc_content = (float(g_count) + float(c_count)) / (total_count - n_count)
g_content = float(g_count) / (total_count - n_count)
c_content = float(c_count) / (total_count - n_count)
at_content = (float(t_count) + float(a_count)) / (total_count - n_count)
a_content = float(a_count) / (total_count - n_count)
t_content = float(t_count) / (total_count - n_count)


if gc_content > 0.6:
    print('The organism is considered “high GC content”')
elif gc_content < 0.4:
    print('The organism is considered “low GC content”')
else:
    print('The organism is considered “moderate GC content”')


# Print the answer
print('GC-content:', gc_content)
print('G-content:', g_content)
print('C-content:', c_content)
print('AT-content:', at_content)
print('A-content:', a_content)
print('T-content:', t_content)
print('Total count:', total_count)
print('Sum of A,T,C,G:', (a_count + t_count + c_count + g_count))
print('Length of sequence:', len(seq))
print('N-content:', n_count)
print('AT/GC ratio:', ((a_count + t_count) / (g_count + c_count)))
