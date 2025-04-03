# Credenciais corretas
usuario_correto = "admin"
senha_correta = "5678"

# Número máximo de tentativas
tentativas_maximas = 3

# Loop para as tentativas de login
for tentativa in range(1, tentativas_maximas + 1):
    print(f"\nTentativa {tentativa} de {tentativas_maximas}")
    
    # Solicitar credenciais ao usuário
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    # Verificar credenciais
    if usuario == usuario_correto and senha == senha_correta:
        print("\nLogin bem-sucedido! Bem-vindo ao sistema.")
        break  # Sai do loop se o login for bem-sucedido
    else:
        tentativas_restantes = tentativas_maximas - tentativa
        if tentativas_restantes > 0:
            print(f"Credenciais incorretas. Você ainda tem {tentativas_restantes} tentativa(s).")
        else:
            print("\nAcesso bloqueado!")
            # Loop para exibir a mensagem de bloqueio 3 vezes
            for _ in range(3):
                print("Acesso bloqueado")      