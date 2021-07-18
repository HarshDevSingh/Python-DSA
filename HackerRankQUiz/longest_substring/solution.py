def findSubstring(s, k):
    # Write your code here
    vowels = ["a", "e", "i", "o", "u"]
    i = 0
    pairs = []
    while i < len(s):
        if k < len(s) + 1:
            pairs.append(s[i:k])
        else:
            break
        k += 1
        i += 1
    di = {}
    for pair in pairs:
        count = 0
        for s in pair:
            if s in vowels:
                count += 1
        di[pair] = count
    vowels_dic={}
    for k in di:
        if di[k]<1:
            continue
        vowels_dic[k]=di[k]
    v = list(vowels_dic.values())
    k = list(vowels_dic.keys())
    if len(v)>0:
        return k[v.index(max(v))]
    return F"not found!"

print(findSubstring("sdfsdf", 5))