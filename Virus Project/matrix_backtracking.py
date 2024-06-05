import matrix_creation
#Backtracking (Part3):
def backtracking(matrix, seq1, seq2):
    seq1_align = ""
    seq2_align = ""
    i = len(seq1)
    j = len(seq2)
    while (i > 0 or j > 0):

        # Checking if it is a match. If it is a match, then append and jump to the diagonal value directly:
        if matrix_creation.match_DNA(seq2[j - 1], seq1[i - 1]):
            seq1_align += seq1[i - 1]
            seq2_align += seq2[j - 1]
            i -= 1
            j -= 1

        # If the sequence don't match:
        else:
            # Creating a temp_list in order to find the maximum values from top, diagonal and left in order to backtrack
            temp_list = [matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]]

            # If the maximum value is the 0th indexed position, i.e., the diagonal value:
            if max(temp_list) == temp_list[0]:
                seq1_align += seq1[i - 1]
                seq2_align += seq2[j - 1]
                i -= 1
                j -= 1

            # If the maximum value is the 1st indexed position, i.e., the top value:
            elif max(temp_list) == temp_list[1]:
                seq1_align += seq1[i - 1]
                seq2_align += "-"
                i -= 1

            # If the maximum value is the 2nd indexed position, i.e., the left vlaue:
            elif max(temp_list) == temp_list[-1]:
                seq1_align += "-"
                seq2_align += seq2[j - 1]
                j -= 1

    # Reverse the string seq1_align
    seq1_align = seq1_align[::-1]
    seq2_align = seq2_align[::-1]
    return seq1_align, seq2_align


def aligment_string(seq1_align, seq2_align):
    # Storing the match, mismatch and gap symbols in match_string:
    match_string = ""
    for i in range(len(seq1_align)):
        if matrix_creation.match_DNA(seq2_align[i], seq1_align[i]):
            match_string += "|"
        elif seq1_align[i] != seq2_align[i]:
            if (seq1_align[i] == "-" or seq2_align[i] == "-"):
                match_string += " "
            else:
                match_string += "*"
    return match_string
