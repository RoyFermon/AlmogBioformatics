from Bio import Align
from Bio import SeqIO


def read_fasta(file):
    """
    Reads a FASTA file and returns the sequence.
    """
    for record in SeqIO.parse(file, "fasta"):
        return str(record.seq)


def global_alignment(seq1, seq2):
    """
    Performs a global alignment between two sequences using Needleman-Wunsch algorithm via PairwiseAligner.
    """
    aligner = Align.PairwiseAligner()
    aligner.mode = 'global'
    aligner.match_score = 1
    aligner.mismatch_score = -1
    aligner.open_gap_score = -1
    aligner.extend_gap_score = -1

    alignments = aligner.align(seq1, seq2)

    max_score = max(len(seq1), len(seq2))
    print("Global alignment:")
    for alignment in alignments:
        print(alignment)
        print("Score:", alignment.score)
        print(f"Match percentage: {100*alignment.score/max_score}%")
        break  # Only display the best alignment


# Read sequences from FASTA files
seq1 = read_fasta("melanocytes-human_skin_cell.fasta")
seq2 = read_fasta("melanocytes-rat_skin_cell.fasta")

# Perform global alignment
global_alignment(seq1, seq2)

