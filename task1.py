A = {1, 2, 3, 4, 6, 7, 9, 10, 11, 13, 14, 17, 24, 26, 28, 29, 31, 32, 34, 35, 37, 38, 39}
B = {1, 2, 4, 10, 12, 13, 15, 17, 18, 19, 25, 30, 33, 34, 35, 36, 37}
C = {2, 7, 9, 14, 16, 21, 23, 25, 27, 28, 29, 32, 34, 35, 36, 37, 38}
D = {1, 3, 5, 6, 9, 10, 14, 15, 19, 21, 23, 28, 29, 31, 34, 35, 36, 37}


def symmetric_difference(set1, set2):
    return (set1 - set2) | (set2 - set1)


def intersection(set1, set2):
    return set1 & set2


def union(set1, set2):
    return set1 | set2


def difference(set1, set2):
    return set1 - set2


# 1. (C ∆ B) ∩ ((C ∆ D) ∪ (A ∆ D)) ∩ ((B ∆ C) ∆ D)
s1 = symmetric_difference(C, B)
s2 = union(symmetric_difference(C, D), symmetric_difference(A, D))
s3 = symmetric_difference(symmetric_difference(B, C), D)

result1 = intersection(s1, s2)
result1 = intersection(result1, s3)

# 2. (C ∩ A ∩ D) ∆ ((A ∩ (B ∆ C) ∩ (D ∆ B)) ∪ ((D \ A) ∆ B))
s4 = intersection(intersection(C, A), D)
s5 = intersection(intersection(A, symmetric_difference(B, C)), symmetric_difference(D, B))
s6 = symmetric_difference(difference(D, A), B)

result2 = symmetric_difference(s4, union(s5, s6))

print("Результат выражения 1:", result1)
print("Результат выражения 2:", result2)
