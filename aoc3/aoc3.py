import string
with open("ao3input.txt") as input1:
    lines=input1.readlines()
alphabets=list(string.ascii_letters)
sums=0
def shared(first,second):
    shareds=list(set(first)&set(second))
    print(shareds)
    sum=0
    for i in shareds:
        for j in range (0,52):
            if (i==alphabets[j]):
                sum+=j+1
    
    print (sum)
    return sum
            
for x in lines:
    first,second=x[:len(x)//2],x[len(x)//2:]
    sums+=shared(first,second)

print(sums)
    