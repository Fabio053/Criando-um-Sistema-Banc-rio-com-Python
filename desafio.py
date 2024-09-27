menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 2000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print("Deposito")

        valor = float(input("Digite o valor a depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n" 
            print(f"Deposito concluido!")
        else:
            print("Valor não permitido, operação cancelada...")

    elif opcao == 2:
        print("Saque")

        valor = float(input("Digite o valor a ser sacado: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saques:
            print("Limite de saques alcançado, tente novamente em 24h")

        elif excedeu_limite:
            print(f"Valor digitado maior que o limite maximo por saque, digite um valor menor que R$ {limite:.2f}")
        
        elif excedeu_saldo:
            print("Saldo insuficiente, digite um valor dentro do saldo atual de sau conta.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: -R$ {valor:.2f}\n"
            print("Saque concluido!")
            numero_saques += 1
        
        else:
            print("Valor não permitido, operação cancelada...")
    
    elif opcao == 3:
        if not extrato:
            print(f"Não foram realizadas transações \n Saldo atual: R${saldo}")
        else:
            print("Extrato")
            print(f"{extrato}\n Saldo atual: R${saldo:.2f}")
    
    elif opcao == 0:
        break

    else:
        print("Digite uma opção valida...")
    