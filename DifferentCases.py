def DifferentCases(strParam): 

    list = []
    strParam2 = ''

    for i in strParam:
        if i.isalpha() and i != '':
            strParam2 += i 
        else: 
            strParam2 = strParam2.lower()
            strParam2 = strParam2.capitalize()
            list += [strParam2]
            strParam2 = ''
        
    strParam2 = strParam2.lower()
    strParam2 = strParam2.capitalize()
    list += [strParam2]
    strParam2 = ''    
    strParam2 = ''.join(list)

    return strParam2

strParam ="-cats And*Dogs-are*AWesome"

# keep this function cali here 
print(DifferentCases(strParam))