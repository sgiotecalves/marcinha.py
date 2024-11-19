##1.	Exercício: Crie um algoritmo que receba 10 números e determine quantos deles são pares.
#pares = 0 
#impares = 0
#for bf in range (10):
#    if int(input("Digite um numero:")) % 2 == 0:
#        pares +=1
#    else:
#        impares += 1       
#print(f"Pares: {pares}\n Impares: {impares}")


#Crie um algoritmo que leia uma lista de números e retorne o maior número que seja menor que 100.


#inp = input("Digite os números separados por espaço: ")
#
#
#numeros = []
#for num in inp.split():
#    numeros.append(int(num))
#
#
#menores_100 = []
#for num in numeros:
#    if num < 100:
#        menores_100.append(num)
#
#
#if menores_100:
#    print(f"O maior número menor que 100 é: {max(menores_100)}")
#else:
#    print("Nenhum número menor que 100 foi encontrado.")

#6.	Exercício: Escreva um programa Python que calcule o quadrado de todos os 
#números de uma lista fornecida pelo usuário.
#entrada = input("Digite os números separados por espaço: ")
#
#quadrados = [int(num) ** 2 for num in entrada.split()]
#
#print("Os quadrados dos números são:", quadrados)

#7.	Exercício: Crie um programa que leia dois números em formato de 
#string e exiba a soma deles como inteiros.


numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

num1 = int(numero1)
num2 = int(numero2)

resultado = num1 + num2

print(f"A soma de {num1} e {num2} é: {resultado}")



    