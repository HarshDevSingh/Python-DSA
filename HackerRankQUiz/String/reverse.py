def reverse(st):
    i=len(st)-1
    rev_st=""
    while i >=0:
        rev_st+=st[i]
        i-=1
    return rev_st
st="this is best"
#print(reverse(st))

words=[]
word=""
for i in range(len(st)):
    if st[i]==" ":
        print(i)
        words.append(word)
        word=""
    else:
        word += st[i]
        if i==len(st)-1:
            words.append(word)




print(words)

