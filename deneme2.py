def EquivalentKeypresses(strArr):
    inp1 = strArr[0].split(",")
    inp2 = strArr[1].split(",")

    idx = []
    for i,key in enumerate(inp1):
        if key == '-B':
            idx.extend([i-1,i])
    
    inp1out =[]
    for j,key in enumerate(inp1):
        if not j in idx and key != '':
            inp1out += key

    idx = []
    for i,key in enumerate(inp2):
        if key == '-B':
            idx.extend([i-1,i])

    inp2out =[]
    for j,key in enumerate(inp2):
        if not j in idx and key != '':
            inp2out += key

    print(inp1out,inp2out)

    return 'true' if inp1out == inp2out else 'false'




EquivalentKeypresses(strArr = (["p,o,i,n,-B,t", "-B,p,o,i,t"]))

