inicio = int(input("Digite um numero para o começo do intervalo :"))
final = int(input("Digite um numero para o final do intervalo :"))

soma_pares = 0

for numero in range(inicio ,final + 1):
    if numero % 2 == 0:
        soma_pares += numero
else:
    if soma_pares == 0 :
        print("Não existem números pares nesse intervalo.")
    else:
        print(f"A soma dos números pares no intervalo de {inicio} ao {final} é : {soma_pares}")        