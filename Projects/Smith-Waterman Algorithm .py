from Bio import Align
from Bio import SeqIO


def read_fasta(file):
    """
    Reads a FASTA file and returns the sequence.
    """
    for record in SeqIO.parse(file, "fasta"):
        return str(record.seq)

def local_alignment(seq1, seq2):
    """
    Performs a local alignment between two sequences using Smith-Waterman algorithm via PairwiseAligner.
    """
    aligner = Align.PairwiseAligner()
    aligner.mode = 'local'
    aligner.match_score = 1
    aligner.mismatch_score = -1
    aligner.open_gap_score = -1
    aligner.extend_gap_score = -1


    alignments = aligner.align(seq1, seq2)

    print("Local alignment:")
    for alignment in alignments:
        print(alignment)
        print("Score:", alignment.score)
        break  # Only display the best alignment


# Read sequences from FASTA files
seq1 = read_fasta("vaccinia virus.fasta")
seq2 = read_fasta("TM250_HUMAN.fasta")

# Perform local alignment
local_alignment(seq1, seq2)
