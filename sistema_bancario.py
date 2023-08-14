menu = """
########-MENU-########
    [1]Depositar
    [2]Sacar
    [3]Extrato
    [4]Novo usuário
    [5]Nova conta
    [0]Sair
########-MENU-########


"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
agencia = "0001"
lista_usuarios = []
lista_contas = []
numero_contas = 0


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$: {valor:.2f}\n"
    else:
        print("Operação falhou, o valor informado é inválido.")
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Número máximo de saques diários atingido.")
    elif valor > limite:
        print("O valor do saque é maior que o limite da conta.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor <= 0:
        print("Valor inválido.")
    else:
        numero_saques += 1

        saldo -= valor
        extrato += f"Saque: R$:{valor:.2f}\n"
        print("Saque de efetuado.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("=====================EXTRATO=====================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$: {saldo:.2f}")
    print("=================================================")


def criar_usuario(lista_usuarios):
    cpf = input("Digite os números do seu CPF:\n")
    for usuario in lista_usuarios:
        if cpf == usuario["cpf"]:
            print("Usuario já cadastrado.")
            return
    nome = input("Digite seu nome.\n")
    data_nasc = input("Digite a data de nascimento\n")
    endereco = input(
        "Digite seu endereço no formato logradouro, numero - bairro - cidade/estado\n"
    )
    lista_usuarios.append(
        {"cpf": cpf, "nome": nome, "data_nasc": data_nasc, "endereco": endereco}
    )
    return


def nova_conta(agencia, numero_contas, lista_usuarios):
    cpf = input("Informe o CPF do titular.\n")
    for usuario in lista_usuarios:
        if cpf == usuario["cpf"]:
            titular = usuario
            numero_contas += 1
            lista_contas.append(
                {"agencia": agencia, "numero_contas": numero_contas, "usuario": titular}
            )
            return print("Conta criada com sucesso!")

    print("CPF não encontrado, crie um usuário antes de criar a conta.")


while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        criar_usuario(lista_usuarios)

    elif opcao == "5":
        nova_conta(agencia, numero_contas, lista_usuarios)

    elif opcao == "0":
        print("Obrigado por utilizar nosso sistema, até a próxima!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
