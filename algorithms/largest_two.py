def largest_two(A):
    my_max, second = A[:2]
    if my_max < second:
        my_max, second = second, my_max

    for idx in range(2, len(A)):
        if my_max < A[idx]:
            my_max, second = A[idx], my_max
        elif second < A[idx]:
            second = A[idx]
    return (my_max, second)


def sorting_two(A):
    return tuple(sorted(A, reverse=True)[:2])


def double_two(A):
    my_max = max(A)
    copy = list(A)
    copy.remove(my_max)
    return (my_max, max(copy))


def mutable_two(A):
    idx = max(range(len(A)), key=A.__getitem__)
    my_max = A[idx]
    del A[idx]
    second = max(A)
    A.insert(idx, my_max)
    return (my_max, second)


def tournament_two(A):
    N = len(A)
    winner = [None] * (N-1)
    loser = [None] * (N-1)
    prior = [-1] * (N-1)

    idx = 0
    for i in range(0, N, 2):
        if A[i] < A[i+1]:
            winner[idx] = A[i+1]
            loser[idx] = A[i]
        else:
            winner[idx] = A[i]
            loser[idx] = A[i+1]
        idx += 1

    m = 0
    while idx < N-1:
        if winner[m] < winner[m+1]:
            winner[idx] = winner[m+1]
            loser[idx] = winner[m]
            prior[idx] = m+1
        else:
            winner[idx] = winner[m]
            loser[idx] = winner[m+1]
            prior[idx] = m
        m += 2
        idx += 1

    largest = winner[m]
    second = loser[m]
    m = prior[m]
    while m >= 0:
        if second < loser[m]:
            second = loser[m]
        m = prior[m]

    return (largest, second)


def two_largest_attempt(A):
    m1 = max(A[:len(A)//2])
    m2 = max(A[len(A)//2:])
    if m1 < m2:
        return (m2, m1)
    return (m1, m2)
