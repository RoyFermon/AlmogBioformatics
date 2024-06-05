def aligment_score(match_string):
    score = 0
    # Calculating the alignment score:
    alignment_score = 0
    for i in range(len(match_string)):
        if match_string[i] == "|":
            alignment_score += 1
        elif (match_string[i] == "*" or match_string[i] == " "):
            alignment_score += -1
    return alignment_score