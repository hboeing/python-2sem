2.Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 20 posições. Crie uma função que receba o vetor preenchido e substitua todas as ocorrências de valores negativos por 0, as de valores menores do que 10 por 1 e as demais por 2.

def altera (vet):
    for i in range(tam):
        if vet[i] < 0:
            vet[i] = 0
        elif vet[i] < 10:
            vet[i] = 1
        else:
            v[i] = 2
    return vet

tam = 3

v = [0] * tam
for i in range(tam):
    v[i] = str(input('Digite um valor: '))
altera(v)
print (v)