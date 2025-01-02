numero_valido = 7
tentativas = 3


print("Esse é um jogo de adivinhação!")
print("Você terá 3 tentativas para adivinhar o número de 1 a 10.")

while tentativas > 0:
    tentativa = int(input("Digite seu número: "))

    if tentativa == numero_valido:
        print('Parabéns! Você acertou o número.')
        break
    else:
        tentativas -=1 
        if tentativas > 0 :
           print('Número incorreto! Tente novamente: ')
        else:
            print("Infelizmente as suas tentativas acabaram. O número certo era 7.")      
else:    
        print("Fim do jogo! ")  