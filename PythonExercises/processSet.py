def process_set(getType,getArray,getProElement):
    if getType=="A":

        if getProElement in getArray:
            return getArray
        else:
            getArray.append(getProElement)
            return getArray
    elif getType=="R":
        if getProElement in getArray:
            getArray.remove(getProElement)
        return getArray

    elif getType=="C":
        if getProElement in getArray:
            return True
        else:
            return False
    else:
        return "invalid"

print process_set('R', [1,2,3], 4)
