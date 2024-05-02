saldo = 500

transacoes = []

saques_realizados = 0

while True:
    operacoes = int(input('''

                ==== BANCO MILENA ===

                Escolha uma das opções

                [1] SALDO

                [2] DEPOSITO

                [3] SAQUE

                [4] EXTRATO

                [5] SAIR

                \n      

                '''))

    if operacoes == 1:

        print(f"Seu saldo é: {saldo} ")

    elif operacoes == 2:

        deposito = float(input("Informe o valor do depósito: "))

        saldo += deposito

        transacoes.append(f"Depósito: R$ {deposito}")

        print(f"Seu saldo é de R$ {saldo}")

    elif operacoes == 3:

        if saques_realizados >= 3:

            print("Não é possível realizar mais saques. Você excedeu o limite de 3 saques diários.")

        else:

            saque = float(input("Informe o valor do saque: "))

            if saque > 500:

                print("Limite máximo de saque por transação é de R$ 500.")

            elif saque > saldo:

                print("Saldo insuficiente.")

            else:

                saldo -= saque

                saques_realizados += 1

                transacoes.append(f"Saque: R$ {saque}")

                print(f"Saque de R$ {saque} realizado com sucesso.")

    elif operacoes == 4:

        print("======== EXTRATO =======")

        for transacao in transacoes:

            print(transacao)

        print("========================")

    elif operacoes == 5:

        print("Saindo do banco...")

        break

    else:

        print("Opção inválida. Por favor, escolha uma opção válida.")
