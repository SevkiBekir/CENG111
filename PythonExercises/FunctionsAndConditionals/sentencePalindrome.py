def ispalindrome(text):
    textLength=len(text)
    newText=""
    newText=newText.join(text)
    
    reverseText=newText[::-1]
    if(newText==reverseText):
        return True
    else:
        return False
