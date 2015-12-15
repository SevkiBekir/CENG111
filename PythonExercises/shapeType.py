import math
def shape_type(array):
    arrayLength=len(array)
    if arrayLength==3: #Triangle
        if isATriangle(array)==False:
            return "not a triangle"
        if array[0]==array[1] or array[0]==array[2] or array[1]==array[2]:
            if array[0]==array[1] and array[1]==array[2]:
                return "equilateral triangle"
            else:
                return "isosceles triangle"
        else:
            return "triangle"
    elif arrayLength==4: #Quadro
        if(array[0]==array[2] and array[1]==array[3]):
            if(array[0]==array[1]):
                return "square"
            else:
                return "rectangle"
        else:
            return "quad"
    else:
        return "not a shape"


def isATriangle(array):
    array.sort()
    maxV=array[2]
    minV=array[0]
    midV=array[1]

    if maxV<minV+midV and maxV>abs(midV-minV):
        return True
    else:
        return False

print shape_type([3,4,8])
