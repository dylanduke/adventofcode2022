import string
with open("ao3input.txt") as input1:
    lines=input1.readlines()
alphabets=list(string.ascii_letters)
sums=0
def shared(first,second,third):
    shareds=list(set(first)&set(second)&set(third))
    print(shareds)
    sum=0
    for i in shareds:
        for j in range (0,52):
            if (i==alphabets[j]):
                sum+=j+1
    
    print (sum)
    return sum
print (len(lines))
x=0
while (x<len(lines)):
    first=lines[x]
    x+=1
    second=lines[x]
    x+=1
    third=lines[x]
    x+=1
    sums+=shared(first,second,third)
    

print(sums)
    