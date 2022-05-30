def atMostNGivenDigitSet(digits, n):
    ans = sum([len(digits) ** i for i in range(1, len(str(n)))])  # Count numbers less than n with digits smaller than len(str(n))
    for i, c in enumerate(str(n)):  # Count the number less than n of digits equal to len(str(n))
        ans += sum([d < c for d in digits]) * len(digits) ** (len(str(n)) - i - 1)
        if c not in digits: break
    return ans + set(str(n)).issubset(digits)  # Finally add 1 if every digit of n comes from the given digits

print(atMostNGivenDigitSet(["1","3","5","7"], 100))
