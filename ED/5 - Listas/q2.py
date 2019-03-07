from lista_estatica import Lista

def merge(l1, l2):
    res = Lista(l1.size+l2.size)

    idx = 0

    while(idx < l1.end or idx < l2.end):
        if(idx < l1.end):
            res.push_back(l1.get(idx))
        if(idx < l2.end):
            res.push_back(l2.get(idx))
        idx+=1
    
    res.print_list()
    return res

l1 = Lista(5)
l2 = Lista(5)

l1.push_back(1)
l1.push_back(3)
l1.push_back(5)
l1.push_back(6)

l2.push_back(2)
l2.push_back(4)

merge(l1,l2)