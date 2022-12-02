with open("aoc1input.txt") as input1:
    lines=input1.readlines()
most=0
runningcount=0
for x in lines:

    if (x!='\n'):

        runningcount+=int(x)
    else:


        if (runningcount>most):

            most=runningcount
        runningcount=0

print(most)


