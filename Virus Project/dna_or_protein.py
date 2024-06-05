def is_dna_rna(sequence:str):
    """Check if the sequence is DNA/RNA."""
    dna_rna_set = set("ACGTUN")
    for char in sequence:
        if char not in dna_rna_set:
            return False
    return True

def is_protein(sequence:str):
    """Check if the sequence is protein."""
    protein_set = set("ACDEFGHIKLMNPQRSTVWYBXZ")
    for char in sequence:
        if char not in protein_set:
            return False
    return True


def dna_or_protein(sequence1:str, sequence2:str):
    if is_dna_rna(sequence1) and is_dna_rna(sequence2):
        return "DNA"
    elif is_protein(sequence1) and is_protein(sequence2):
        return "protein"
    else:
        exit(0)