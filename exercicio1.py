1.Dada uma sequ�ncia de n�meros inteiros maiores que 1, terminando por 0, determine quantos n�meros primos h� nela. Crie uma fun��o car para determinar os n�meros primos.

num = int(input("Digite um numero (0 para terminar): "))

cont = 0
while num != 0:
    primo = True
    i = 2
    while i < num and primo:
        if num % i == 0:
            primo = False
        i += 1
    if primo:
        cont += 1

    num = int(input("Digite um numero (0 para terminar): "))

print("Achei %d primos na sequencia" % (cont))
