def mult_matrix(a,b):
    res = []
    for i in range(0,len(a)):
        lin = []
        for j in range(0, len(b[0])):
            lin.append(0)
            for k in range(0,len(a[i])):
                #print("res[%d][%d](%d) += %d"%(i,j,res[i][j],a[i][k]*b[k][j]))
                lin[j] += a[i][k]*b[k][j]
        res.append(lin)
    return res
