import math
def process_vector(myType, vector):
    magV1=math.sqrt(square(vector[0][0])+square(vector[0][1])+square(vector[0][2]))
    if myType=="SM":
        magV2=math.sqrt(square(vector[1][0])+square(vector[1][1])+square(vector[1][2]))
        return magV1*magV2
    elif myType=="M":
        return magV1
    elif myType=="N":
        return (vector[0][0]/magV1,vector[0][1]/magV1,vector[0][2]/magV1)


def square(number):
    return number*number

print process_vector("SM", [(3.0, 4.0, 5.0), (2.0, 4.0, 6.0)])
