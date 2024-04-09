print("\nSeja bem vindo, escolha uma das opções abaixo:")
menu = """
#############

[d]epositar
[s]acar
[e]xtrato
[f]echar

#############
"""

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":

        print("Depósito escolhido\n")
        deposito = float(input("Digite o valor que deseja depositar:"))
        if deposito < 0:
            print("Valor inválido!")
        else:
            saldo += deposito
            print(f"\nO valor de R${deposito:.2f} foi depositado na sua conta.")
            print(f"\nSeu saldo atual é de R${saldo:.2f}")
            extrato += f"Depósito: +R${deposito:.2f}\n"

    elif opcao == "s":

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


    elif opcao == "e":

        print("\nExtrato escolhido.\n")
        print("Extrato:")
        if extrato == "":
            print("Não foram realizadas movimentações\n")
        else:
            print(extrato)
        print(f"Seu saldo atual é de R${saldo:.2f}")
        
    elif opcao == "f":
        print("Saindo da aplicação.")
        break
    else:
        print("Opção escolhida inválida, por favor escolha uma opção válida!")