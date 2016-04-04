def translate(text):
    textLength=len(text)
    if textLength==15:
        if text[0:3]!="AUG":
            return "start codon not recognized"
        if text[12:]=="UAA" or text[12:]=="UGA" or text[12:]=="UAG":

            array=[]
            for i in range(0,3):
                array.append(findRNA(text[3*i+3:3*i+6]))
            return array
        else:
            return "stop codon not recognized"




def findRNA(text):
    RNAList=[['UUU','Phenylalanine'],['UUA','Leucine'],['AUU','Isoleucine'],['GUU', 'Valine'],['UCU','Serine']]
    for i in range(0,5):
        if text==RNAList[i][0]:
            return RNAList[i][1]

print translate('AUGUCUGUUAUUUGA')
