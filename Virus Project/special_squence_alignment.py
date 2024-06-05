from Bio import SeqIO

import dna_or_protein
import matrix_backtracking
import matrix_creation
import score



def read_fasta(file):
    """
    Reads a FASTA file and returns the sequence.
    """
    for record in SeqIO.parse(file, "fasta"):
        return str(record.seq)

def sequence_alignment(seq1_fasta, seq2_fasta):

    seq1 = read_fasta(seq1_fasta)
    seq2 = read_fasta(seq2_fasta)

    sequence_type = dna_or_protein.dna_or_protein(seq1, seq2)
    print("The given files are " + str(sequence_type) + " sequences, lets compare them:")

    matrix = matrix_creation.create_matrix(seq1, seq2, 1, -1 , -1)

    seq1_align, seq2_align = matrix_backtracking.backtracking(matrix, seq1, seq2)
    match_string = matrix_backtracking.aligment_string(seq1_align, seq2_align)

    alignment_score = score.aligment_score(match_string)
    max_score = max(len(seq1), len(seq2))
    return alignment_score, max_score

Mean_Lettuce_fasta = "BadLettuce.fasta"
Mother_fasta = {"Lettuce1.fasta", "Lettuce2.fasta", "Lettuce3.fasta", "Lettuce4.fasta", "Lettuce5.fasta"}

dict = {}
for mother in Mother_fasta:
    alignment_score, max_score = sequence_alignment(Mean_Lettuce_fasta, mother)
    dict[mother] = alignment_score
    print(mother + ":\nscore:" + str(alignment_score))
    print(f"Match percentage: {100 * alignment_score / max_score}%")

max_score_all = max(dict.values())
for mother in dict:
    if dict[mother] == max_score_all:
        print(f"\n\n\nThe real mother of the evil lettuce is:\n {mother}")