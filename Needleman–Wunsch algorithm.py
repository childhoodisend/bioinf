import numpy as np


def print_matrix(mat):
    for el in mat:
        print(*el)


def S(c1: str, c2: str) -> int:
    if c1 == c2:
        return 1
    else:
        return -1


def get_patterns(pattern1: str, pattern2: str, M: np.matrix, n: int, m: int) -> (str, str):
    i = n
    j = m
    string1 = ""
    string2 = ""
    while i > 0 and j > 0:
        cur_score = M[i, j]
        diag_score = M[i - 1, j - 1]
        left_score = M[i - 1, j]
        up_score = M[i, j - 1]
        if cur_score == diag_score + S(pattern1[i - 1], pattern2[j - 1]):
            string1 += pattern1[i - 1]
            string2 += pattern2[j - 1]
            j -= 1
            i -= 1
        elif cur_score == left_score - 1:
            string1 += pattern1[i - 1]
            string2 += "_"
            i -= 1
        elif cur_score == up_score - 1:
            string1 += "-"
            string2 += pattern2[j - 1]
            j -= 1
    while i > 0:
        string1 += pattern1[i - 1]
        string2 += "_"
        i -= 1
    while j > 0:
        string2 += pattern2[j - 1]
        string1 += "_"
        j -= 1

    string1 = string1[::-1]
    string2 = string2[::-1]
    return string1, string2


def needleman_wunsch(pattern1: str, pattern2: str, M: np.matrix):
    n = len(pattern1)
    m = len(pattern2)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = M[i - 1, j - 1] + S(pattern1[i - 1], pattern2[j - 1])
            delete = M[i - 1, j] + S(pattern1[i - 1], "_")
            insert = M[i, j - 1] + S("_", pattern2[j - 1])
            M[i, j] = max(match, delete, insert)
    print_matrix(M)
    return get_patterns(pattern1, pattern2, M, n, m)


pat1 = "ACGTTAG"
pat2 = "ACCTAG"
n = len(pat1)
m = len(pat2)
M = np.zeros((n + 1, m + 1))

for i in range(n + 1):
    for j in range(m + 1):
        M[0, j] = -j
        M[i, 0] = -i

first_str, second_str = needleman_wunsch(pat1, pat2, M)
print("-> {}\n-> {}".format(first_str, second_str))
