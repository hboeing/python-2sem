3. Crie um algoritmo que solicite 3 valores que representarão os lados de um triângulo. Considere que não importa a ordem em que serão fornecidos os valores, podendo ser fornecido primeiramente a hipotenusa e depois os catetos ou os catetos e depois a hipotenusa etc. Crie também uma função que recebe o vetor e retorne se os lados informados formam um triângulo retângulo. Você pode utilizar o teorema de Pitágoras para auxiliar na resolução: hipotenusa2 = cateto12 + cateto22.

import math

def triangret(vet):
    if vet[0] > vet[1] and vet[0] > vet[2]:
        hip = vet[0]
        cat1 = vet[1]
        cat2 = vet[2]
    elif vet[1] > vet[0] and vet[1] > vet[2]:
        hip = vet[1]
        cat1 = vet[0]
        cat2 = vet[2]
    else:
        hip = vet[2]
        cat1 = vet[0]
        cat2 = vet[1]
    print(hip, cat1, cat2)

    if hip == math.sqrt(cat1**2 + cat2**2):
        return 1
    else:
        return 0

vet = [0]*3
for i in range(3):
    vet[i] = input('Digite um valor: ')

if triangret(vet) == 1:
    print('É retangulo')
else:
     print('Não é retangulo')
