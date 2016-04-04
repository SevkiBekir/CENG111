def process_shape(array):
    myType=array[0]
    n1=array[1]
    if myType=="S":
        return 4*n1
    elif myType=="R" or myType=="T":
        n2=array[2]
        if myType=="R":
            return 2*n1+2*n2
        if myType=="T":
            n3=array[3]
            return n1+n2+n3
    else:
        print "ERROR!!"

print process_shape(['S', 5])
