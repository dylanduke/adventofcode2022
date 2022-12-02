with open("aoc2input.txt") as input1:
    lines=input1.readlines()
count=0
for x in lines:
    if(x[2]=='Z'):
        count+=6
        if(x[0]=='A'):
            count+=2
            continue
        if(x[0]=='B'):
            count+=3
            continue
        if(x[0]=='C'):
            count+=1
            continue
    if(x[2]=='Y'):
        count+=3
        if(x[0]=='A'):
            count+=1
            continue
        if(x[0]=='B'):
            count+=2
            continue
        if(x[0]=='C'):
            count+=3
            continue
    if(x[2]=='X'):
        if(x[0]=='A'):
            count+=3
            continue
        if(x[0]=='B'):
            count+=1
            continue
        if(x[0]=='C'):
            count+=2
            continue
    
print(count)