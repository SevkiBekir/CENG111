import math
def arithmetic(array):
    myType=array[0]
    n1=array[1]
    n2=array[2]
    if myType=="add":
        return n1+n2
    elif myType=="minus":
        return n1-n2
    elif myType=="mult":
        return n1*n2
    elif myType=="div":
        return n1/n2
    elif myType=="max":
        return max(n1,n2)
    elif myType=="min":
        return min(n1,n2)

print arithmetic(['add', 3, 5])
