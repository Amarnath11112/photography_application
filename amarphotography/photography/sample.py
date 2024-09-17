
def first_last(lis):
    first=lis[0]
    last=lis[-1]
    if first==last:
        return True
    else:
        return False


lis=[10,20,30,40,50,10]
output=first_last(lis)
print(output)

stri="adagaaggddaadumpdddpu"

def words(string123):
    counts=dict()
    words=string123.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] =1
    return counts

print(words('the quick brown fox jumps over the lazy dc'))


def fibnocci(n):
    if n==1 or n==2:
        return 1
    else:
        return(fibnocci(n-1)+fibnocci(n-2))

print(fibnocci(7))









