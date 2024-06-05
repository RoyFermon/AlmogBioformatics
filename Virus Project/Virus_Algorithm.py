from Bio import SeqIO

import dna_or_protein
import matrix_backtracking
import matrix_creation
import score

seq1_fasta = "BadLettuce.fasta"
seq2_fasta = "Lettuce1.fasta"

def read_fasta(file):
    """
    Reads a FASTA file and returns the sequence.
    """
    for record in SeqIO.parse(file, "fasta"):
        return str(record.seq)


seq1 = read_fasta(seq1_fasta)
seq2 = read_fasta(seq2_fasta)

sequence_type = dna_or_protein.dna_or_protein(seq1, seq2)
print("The given files are " + str(sequence_type) + " sequences, lets compare them:")

matrix = matrix_creation.create_matrix(seq1, seq2, 1, -1 , -1)

seq1_align, seq2_align = matrix_backtracking.backtracking(matrix, seq1, seq2)
match_string = matrix_backtracking.aligment_string(seq1_align, seq2_align)

alignment_score = score.aligment_score(match_string)

#Printing out the final result:
print(seq1_align)
print(match_string)
print(seq2_align)
print("Alignment score:", alignment_score)

max_score = max(len(seq1), len(seq2))
print(f"Match percentage: {100 * alignment_score/max_score}%")