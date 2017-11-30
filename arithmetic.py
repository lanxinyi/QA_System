# -*- coding: utf-8 -*-

class arithmetic():
    def __init__(self):
        pass

    def levenshtein(self, first, second):
        if len(first) > len(second):
            first,second = second, first
        if len(first) == 0:
            return len(second)
        if len(second) == 0:
            return len(first)

        first_length = len(first) + 1
        second_length = len(second) + 1
        distance_matrix = [range(second_length) for x in range(first_length)]
        for i in range(1, first_length):
            for j in range(1, second_length):
                deletion = distance_matrix[i-1][j] + 1
                insertion = distance_matrix[i][j-1] + 1
                substitution = distance_matrix[i-1][j-1]
                if first[i-1] != second[j-1]:
                    substitution += 1
                distance_matrix[i][j] = min(deletion, insertion, substitution)

        return distance_matrix


    def lcs(self, first, second):
        n = len(first)
        m = len(second)
        if n == 0 or m == 0:
            return ""

        l = [([0] * (m + 1)) for _ in range(n + 1)]
        direct = [([0] * m) for _ in range(n)]  # 0 for top left, -1 for left, 1 for top

        for i in range(n + 1)[1:]:
            for j in range(m + 1)[1:]:
                if first[i - 1] == second[j - 1]:
                    l[i][j] = l[i - 1][j - 1] + 1
                elif l[i][j - 1] > l[i - 1][j]:
                    l[i][j] = l[i][j - 1]
                    direct[i - 1][j - 1] = -1
                else:
                    l[i][j] = l[i - 1][j]
                    direct[i - 1][j - 1] = 1

        i, j = n - 1, m - 1
        lcs = []
        while i >= 0 and j >= 0:
            if direct[i][j] == 0:
                lcs.append(first[i])
                i -= 1
                j -= 1
            elif direct[i][j] == 1:
                i -= 1
            else:
                j -= 1

        return "".join(lcs)[::-1]
