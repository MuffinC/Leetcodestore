def partitionLabels(s):

    hash = {}

    for x, y in enumerate(s):
        if y not in hash:
            hash[y] = x
        else:
            hash[y] = x
            

    return hash

print(partitionLabels("ababcbacadefegdehijhklij"))