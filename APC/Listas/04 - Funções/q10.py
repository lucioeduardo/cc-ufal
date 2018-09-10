"""
Faça um programa que recebe duas palavras
a e b e verifica se b é um segmento de a.
"""

def eh_segmento(a, b):
    for i in range(0,len(a)):
        idx_b = 0
        for j in range(i,len(a)):
            if(a[j] == b[idx_b]):
                idx_b+=1
            else:
                break
            if(idx_b == len(b)):
                return True
    return False

def kmp(a, b):
    i = 0
    j = 0

    while(i < len(a)):
        if(a[i] == b[j]):
            i+=1
            j+=1
        else:
            if(j == 0):
                i+=1
                continue
            j-=1

        if(j == len(b)):
            return True
    return False


print(eh_segmento("avisar","vida"))
print(kmp("cabonera","cabonera"))
