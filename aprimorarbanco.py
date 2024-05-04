saldo = 500
transacoes = []
saques_realizados = 0
usuarios = []
contas = []
numero_conta = 1

def consultar_saldo():
    print(f"Seu saldo é: {saldo} ")

def fazer_deposito():
    global saldo
    deposito = float(input("Por favor, informe o valor do depósito: "))
    saldo += deposito
    transacoes.append(f"Depósito realizado: R$ {deposito}")
    print(f"Seu saldo é de R$ {saldo}")

def fazer_saque():
    global saldo, saques_realizados
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

def mostrar_extrato():
    print("======== EXTRATO =======")
    for transacao in transacoes:
        print(transacao)
    print("========================")

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = input("Digite o endereço do usuário (logradouro, número, bairro, cidade/estado): ")
    # Verifica se já existe um usuário com o mesmo CPF
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: Já existe um usuário com este CPF.")
            return
  
    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
 
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso.")

def criar_conta():
    global numero_conta
    cpf = input("Digite o CPF do usuário para criar a conta: ")
    
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if usuario is None:
        print("Erro: Usuário com este CPF não existe.")
        return
    
    nova_conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': cpf
    }
    
    contas.append(nova_conta)
    print(f"Conta criada com sucesso. Número da conta: {numero_conta}")
    numero_conta += 1

while True:
    operacao = int(input('''

                ==== BANCO MILENA ===

                       BEM VINDO

                Escolha uma das opções

                [1] SALDO

                [2] DEPOSITO

                [3] SAQUE

                [4] EXTRATO

                [5] CRIAR USUÁRIO

                [6] CRIAR CONTA

                [7] SAIR

                \n      

                '''))

    if operacao == 1:
        consultar_saldo()
    elif operacao == 2:
        fazer_deposito()
    elif operacao == 3:
        fazer_saque()
    elif operacao == 4:
        mostrar_extrato()
    elif operacao == 5:
        criar_usuario()
    elif operacao == 6:
        criar_conta()
    elif operacao == 7:
        print("Saindo do banco. Até Breve")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
