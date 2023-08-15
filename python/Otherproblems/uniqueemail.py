def numUniqueEmails(emails):
    res = []
    for x in emails:
        start = 0
        act=0
        for z, y in enumerate(x):
            if y == '+' and act==0:
                start=z
                act=1
            if y == '@':
                if act==1:
                    loc = "".join(x[:start])
                else:
                    loc="".join(x[:z])

                loc=loc.replace('.','')
                dom = "".join(x[z + 1:])
                break

        res.append(loc +'@' +dom)
    return len(set(res))

print(numUniqueEmails(["test.emailalex@leetcode.com","test.e.mailbob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))