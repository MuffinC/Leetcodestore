def intToRoman(num: int) -> str:
    mapping = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
               'CM': 900, 'M': 1000}
    output = ''
    for i in reversed(mapping):
        while num >= mapping[i]:
            num -= mapping[i]
            output += i

    return output
print(intToRoman(58))