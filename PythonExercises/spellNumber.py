def spell(number):
    arrayOnlar=["on","yirmi","otuz","kirk","elli","altmis","yetmis","seksen","doksan"]
    arrayBirler=["bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz"]
    getOnlar=number/10
    getBirler=number%10
    array=[]
    if getOnlar!=0 or getBirler!=0:
        if getOnlar!=0 and getBirler!=0:
            array.append(arrayOnlar[getOnlar-1])
            array.append(arrayBirler[getBirler-1])
        elif getOnlar==0:
            array.append(arrayBirler[getBirler-1])
        elif getBirler==0:
            array.append(arrayOnlar[getOnlar-1])
        return array

print spell(34)
