def EquivalentKeypresses(strArr):
    a, b =  map(lambda x: x.split(','), strArr)

    print(a, b)

    mark_for_deletion = []
    for pos, key_press in enumerate(a):
        if key_press == '-B':
            mark_for_deletion.extend([pos-1, pos])
    a = [l for p, l in enumerate(a) if not p in mark_for_deletion and l != '']
    
    mark_for_deletion = []
    for pos, key_press in enumerate(b):
        if key_press == '-B':
            mark_for_deletion.extend([pos-1, pos])
            print('Markdel = ', mark_for_deletion)
    b = [l for p, l in enumerate(b) if not p in mark_for_deletion and l != '']

    print(a, b)
    print(len(a), len(b))
    return 'true' if a == b else 'false'

EquivalentKeypresses(["q,w,e,r,t,y", "-B,-B,q,w,w,-B,e,r,t,y"])
EquivalentKeypresses(["p,o,i,n,-B,t", "-B,p,o,i,t"])
EquivalentKeypresses(["s,t,r,e,e,t", "-B,s,s,-B,t,r,e,e,t"])
EquivalentKeypresses(["a,b,c,d", "a,b,c,d,-B,e"])