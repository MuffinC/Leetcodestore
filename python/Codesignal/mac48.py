def solution(inputString):
    table=inputString.split('-')
    if len(table) !=6: return False
    start=ord('A')
    stop=ord('F')
    for word in table:
        if word[1].isalpha():
            if  not ord(word[1])>=start or not ord(word[1])<=stop: return False
        if word[0].isalpha():
            if not ord(word[0])>=start or not ord(word[0])<=stop: return False



        if len(word) !=2:
            return False
    return True

print(solution("00-1B-63-84-45-E6"))