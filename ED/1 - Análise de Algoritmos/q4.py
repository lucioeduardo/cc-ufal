"""
4. Identificar a soma máxima entre dois elementos de um
conjunto

*** Análise ***
Operação principal: comparação i > m_1
T(n) = n
"""

conj = [1,5,2,50,1,90,3,15,100,91]

soma = conj[0]
m_1 = -999999
m_2 = -999999
for i in conj:
    if(i > m_1):
        m_2 = m_1
        m_1 = i
    elif(i > m_2):
        m_2 = i


print(m_1 + m_2)
