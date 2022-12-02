with open("aoc2input.txt") as input1:
    lines=input1.readlines()
count=0
for x in lines:
    #x.strip()
    if(x[2]=='Z'):
        count+=3
        if(x[0]=='A'):
            continue
        if(x[0]=='B'):
            count+=6
            continue
        if(x[0]=='C'):
            count+=3
            continue
    if(x[2]=='Y'):
        count+=2
        if(x[0]=='A'):
            count+=6
            continue
        if(x[0]=='B'):
            count+=3
            continue
        if(x[0]=='C'):
            continue
    if(x[2]=='X'):
        count+=1
        if(x[0]=='A'):
            count+=3
            continue
        if(x[0]=='B'):
            continue
        if(x[0]=='C'):
            count+=6
            continue
    
print(count)