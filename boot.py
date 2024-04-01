inicio = """
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Encerrar

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
ERRO = "Operação não realizada!"

while True:
    opcao = input(inicio)
    if opcao == "1":
        valor = float(input("informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
            print(f"\nDepósito de R$ {valor:.2f} realizado")
        else:
            print(ERRO + " O valor informado é inválido.")
    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print(ERRO + " O saldo insuficiente em conta.")
        elif excedeu_limite:
            print(ERRO + f" O valor máximo diário de {limite:.2f} por operação ultrapassado.")
        elif excedeu_saques:
            print(ERRO + f" São permitidos somente {LIMITE_SAQUES} saques diários.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\nSaque de {valor:.2f} realizado.")
            print(f"\nRestam ainda {LIMITE_SAQUES-numero_saques} saques a serem realizados hoje")
        else:
            print(ERRO + " O valor informação inválido")
    elif opcao == "3":
        print("\n---------------------EXTRATO---------------------")
        print("Não há movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("\n---------------------EXTRATO---------------------")
    elif opcao == "4":
        break
    else:
        print(ERRO + " Opção inválida")
