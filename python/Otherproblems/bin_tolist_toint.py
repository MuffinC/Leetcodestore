
head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
counter =0
result = 0
for x in reversed(head):

    if (x == 1):
        result = result + 2**counter

    counter +=1

print(result)