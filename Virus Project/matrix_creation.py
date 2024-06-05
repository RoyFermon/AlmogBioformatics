def match_DNA(a, b):
    dna_rna_set = set("ACGTUN")
    if a not in dna_rna_set or b not in dna_rna_set:
        return a == b
    if a == 'A' and b == 'T':
        return True
    if a == 'T' and b == 'C':
        return True
    if a == 'C' and b == 'G':
        return True
    if a == 'G' and b == 'A':
        return True
    if a == 'N' and b == 'N':
        return True
    return False

def init_matrix(gap, n, m):
    init_mat = []  # Initialised matrix
    #Initialising the matrix to 0 (Part1):
    for i in range(m+1):
        temp = []
        for j in range(n+1):
            temp.append(0)
        init_mat.append(temp)

    for j in range(n+1):
        init_mat[0][j] = gap*j

    for i in range(m+1):
        init_mat[i][0] = gap*i
    return init_mat

def fill_matrix(matrix, seq1, seq2, match, mismatch, starting_gap):
    n = len(seq2)
    m = len(seq1)

    current_gap = starting_gap
    #Matrix filling (Part2):
    for i in range(1,m+1):
        for j in range(1, n+1):
            if match_DNA(seq2[j-1], seq1[i-1]):
                matrix[i][j] = max(matrix[i][j-1]+current_gap, matrix[i-1][j]+current_gap, matrix[i-1][j-1]+match)
            else:
                matrix[i][j] = max(matrix[i][j-1]+current_gap, matrix[i-1][j]+current_gap, matrix[i-1][j-1]+mismatch)
    return matrix

def create_matrix(seq1, seq2, match, mismatch, gap):
    matrix = init_matrix(gap, len(seq2), len(seq1))
    return fill_matrix(matrix, seq1, seq2, match, mismatch, gap)