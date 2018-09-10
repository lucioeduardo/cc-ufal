"""
Validar CPF
"""

def mult_desc(lista, mult):
    res = 0
    for i in range(mult,1,-1):
        res += int(lista[mult-i]) * i
    return res

def valida(cpf):
    soma = mult_desc(cpf, 10)
    soma*=10
    resto = (soma%11)%10

    if(resto != int(cpf[9])):
        return False

    soma = mult_desc(cpf, 11)
    soma*=10
    resto = (soma%11)%10

    if(resto != int(cpf[10])):
        return False

    return True


cpf = "12345678909"
print(valida(cpf))
