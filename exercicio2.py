2.Fa�a um algoritmo que solicite ao usu�rio n�meros e os armazene em um vetor de 20 posi��es. Crie uma fun��o que receba o vetor preenchido e substitua todas as ocorr�ncias de valores negativos por 0, as de valores menores do que 10 por 1 e as demais por 2.

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