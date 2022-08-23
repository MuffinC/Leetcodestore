def solution(n):
    a = [1] + [0] * n
    for i in range(1, n + 1):
        for k in reversed(range(i, n + 1)):
            a[k] = a[k - i] + a[k]
    return a[n] - 1


print(solution(5))