def tribonacci(n):
    alpha = 0
    beta = 1
    gamma = 1
    if n == 0:
        return alpha
    elif n <=2:
        return beta
    else:
        for x in range(2, n, 1):
            prev1 = gamma
            prev2 = beta
            gamma = alpha + beta + gamma
            alpha = prev2
            beta = prev1
        return gamma

print(tribonacci(25))