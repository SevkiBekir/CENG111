def fibseries(number):
    if number==1 or number==0:
        return []
    else:
       newThing=fibseries(number-1) + fibseries(number-2)
       return [newThing]

print fibseries(5)
