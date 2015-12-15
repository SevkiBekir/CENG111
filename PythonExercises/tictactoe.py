def tictactoe(array):
    for i in range(0,len(array)):
        print "array[0][",i,"]:",array[0][i],"array[1][",i,"]:",array[1][i],"array[2][",i,"]:",array[2][i]
        print "array[",i,"][0]",array[i][0],"array[",i,"][1]:",array[i][1],"array[",i,"][2]:",array[i][2]
        if (array[0][i]==array[1][i] and array[0][i]==array[2][i]) or (array[i][0]==array[i][1] and array[i][0]==array[i][2]): #VERTICAL or #HORIZANTAL
            print "girdi"
            if array[0][i]==array[1][i] and array[0][i]==array[2][i]:
                return array[0][i]
            elif array[i][0]==array[i][1] and array[i][0]==array[i][2]:
                return array[i][0]
        else:
            continue
    return "tie"


print tictactoe(['XOX', 'OOX', 'XXO'])
print tictactoe(['XXO', 'OOX', 'XXX'])
print tictactoe(['XOO', 'XOX', 'XXO'])
print tictactoe(['XOO', 'XOO', 'OXO'])
