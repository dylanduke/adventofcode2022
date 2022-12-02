with open("aoc1input.txt") as input1:
    lines=input1.readlines()
least=0
next=0
most=0
runningcount=0
for x in lines:
    if (x!='\n'):
        runningcount+=int(x)
    else:
        if (runningcount>least):
            least=runningcount
            if(least>next):
                temp=next
                next=least
                least=temp
            if(next>most):
                temp=most
                most=next
                next=temp
        runningcount=0
                
print(least+next+most)
                
                

