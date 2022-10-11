def check(A, i, n):
    a = 0
    b = 0
    if A == 0:
        a = n
        b = (i + 1) // n
    else:
        a = A
        b = (i + 1) // n + 1
    return [a, b]


def solution(n, words):
    l = len(words)
    w_c = {}

    for i in set(words):
        w_c[i] = 0

    w_c[words[0]] = 1
    for i in range(1, l):
        w_c[words[i]] += 1
        if words[i - 1][-1] != words[i][0] or w_c[words[i]] > 1:
            A = (i + 1) % n
            return check(A, i, n)

    return [0, 0]