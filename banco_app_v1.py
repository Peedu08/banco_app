def menu_de_opcoes():
    
    print("""
    #############

    [C] 👤 Cadastrar usuário
    [N] 💰 Nova Conta
    [D] 💵 Depositar
    [S] 💸 Sacar
    [E] 📃 Extrato
    [L] 📖 Listar Contas
    [F] 🚪 Fechar

    #############
    """)

def mensagem_boas_vindas():
    print("\nSeja bem vindo, escolha uma das opções abaixo:")

def cadastrar_usuario(usuarios):
    fazer_cadastro = input("Cadastrar novo usuário? (S/N): ")
    if fazer_cadastro.upper() == "N":
        print("Voltando ao menu principal!")
        pass
    elif fazer_cadastro.upper() == "S":
        print("Vamos pedir algumas informações para o novo cadastro.")
        cpf = input("Digite o CPF (somente números): ")
        usuario = filtrar_usuario(cpf, usuarios)
        if usuario:
            print("CPF já cadastrado")
            return
        nome = input("Digite seu nome completo: ").capitalize()
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
        endereco = input("Digite o endereço (logradouro, número - bairro - cidade/estado): ")
        
        usuarios.append({'cpf': cpf, 'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco})

        print('Usuário cadastrado.')
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = []
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios_filtrados.append(usuario)
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input('Digite o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print('Usuário não encontrado, voltando ao menu principal.')
        return

    # Verificando se o usuário já possui uma conta
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf:
            print('O usuário já possui uma conta.')
            return

    print('Conta cadastrada com sucesso!')
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})

def listar_contas(contas):
    print("\n================ LISTA DE CONTAS ================")
    for conta in contas:
        print(f"Agência:\t{conta['agencia']}\nC/C:\t\t{conta['numero_conta']}\nTitular:\t{conta['usuario']['nome']}")
        print("=" * 50)

def saque(*, saldo, limite_valor_saque, numero_saques, LIMITE_SAQUES, extrato):
    print("\nSaque escolhido.\n")
    saque = float(input("Digite o valor que deseja sacar:"))
    if saque < 0 or saque > saldo:
        print("Valor do saque inválido ou saldo insuficiente!")
    elif numero_saques >= LIMITE_SAQUES:
        print("Você atingiu o limite máximo de saques!")
    elif saque > limite_valor_saque:
        print(f"Limite para cada saque é de R${limite_valor_saque:.2f}")
    else:
        saldo -= saque
        print(f"O valor de R${saque:.2f} foi sacado da sua conta.")
        print(f"Seu saldo atual é de R${saldo:.2f}")
        numero_saques += 1
        extrato += f"Saque: -R${saque:.2f}\n"
    return saldo, limite_valor_saque, numero_saques, LIMITE_SAQUES, extrato

def depositar(saldo, extrato, /):
    print("Depósito escolhido\n")
    deposito = float(input("Digite o valor que deseja depositar:"))
    if deposito < 0:
        print("Valor inválido!")
    else:
        saldo += deposito
        print(f"\nO valor de R${deposito:.2f} foi depositado na sua conta.")
        print(f"\nSeu saldo atual é de R${saldo:.2f}")
        extrato += f"Depósito: +R${deposito:.2f}\n"
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\nExtrato escolhido.\n")
    print("Extrato:")
    if extrato == "":
        print("Não foram realizadas movimentações\n")
    else:
        print(extrato)
    print(f"Seu saldo atual é de R${saldo:.2f}")
    return extrato


def main():

    usuarios = []
    contas = []
    NUMERO_AGENCIA = "0001"
    saldo = 0
    limite_valor_saque = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        menu_de_opcoes()   

        opcao = input()

        if opcao.upper() == "C":
            cadastrar_usuario(usuarios)

        elif opcao.upper() == "N":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(NUMERO_AGENCIA, numero_conta, usuarios, contas)
            if conta:
                contas.append(conta)

        elif opcao.upper() == "D":
            saldo, extrato = depositar(saldo, extrato)
            

        elif opcao.upper() == "S":
            numero_saques = int(numero_saques)
            saldo, limite_valor_saque, numero_saques, LIMITE_SAQUES, extrato = saque(saldo=saldo, limite_valor_saque=limite_valor_saque, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES, extrato=extrato)

            
        elif opcao.upper() == "E":
            extrato = exibir_extrato(saldo, extrato = extrato)

        elif opcao.upper() == "L":
            listar_contas(contas)        
            
        elif opcao.upper() == "F":
            print("Saindo da aplicação.")
            break
        else:
            print("Opção escolhida inválida, por favor escolha uma opção válida!")

        input('\nPressione Enter para continuar...')
        print('\n'* 50)

mensagem_boas_vindas()
main()