
menu = """
Escolha uma das opções:
[a] Depositar
[b] Sacar
[c] Extrato
[nu] Novo usuário
[nc] Criar conta
[lc] Listar contas
[d] Sair
==> """

AGENCIA = '0001'
LIMITE_SAQUE = 3
saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
numero_da_conta = 0
usuarios = []
contas = []

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito de R$ {valor:.2f}\n'
        print(f'R$ {valor:.2f} Reais depositados com sucesso.')
        print('-' * 40)
    else:
        print('Valor inválido.')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_de_saques, LIMITE_SAQUE):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_de_saques >= LIMITE_SAQUE

    if excedeu_saldo:
        print('A operação falhou! Você não tem saldo suficiente.')
    elif excedeu_limite:
        print('A operação falhou! Limite de saque excedido.')
    elif excedeu_saques:
        print('A operação falhou! Número máximo de saques excedido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque no valor de R$ {valor:.2f}\n'
        print(f'Saque de R$ {valor:.2f} Reais realizado com sucesso.')
        numero_de_saques += 1
        print('-' * 40)
    else:
        print('A operação falhou! Valor informado inválido.')
    return saldo, extrato, numero_de_saques

def mostrar_extrato(saldo, /, *, extrato):
    print('\n===============EXTRATO===============')
    print('Não foram realizadas transações.' if not extrato else extrato)
    print(f'Saldo: R$ {saldo:.2f}')
    print('=====================================')

def criar_usuario(usuarios):
    cpf = input('Informe o número do CPF: ')
    usuario_filtrado = filtrar_usuario(cpf, usuarios)
    if usuario_filtrado:
        print('Já existe usuário com esse CPF.')
        return

    nome = input('Informe o nome completo: ')
    data_de_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
    endereco = input('Informe o endereço (Logradouro, N - Bairro - Cidade/Sigla Estado): ')

    usuarios.append({'nome': nome, 'cpf': cpf, 'data_de_nascimento': data_de_nascimento, 'endereco': endereco})
    print('Usuário criado com sucesso.')

def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(AGENCIA, numero_da_conta, usuarios):
    cpf = input('Informe seu CPF: ')
    usuario_filtrado = filtrar_usuario(cpf, usuarios)
    if usuario_filtrado:
        print('Conta criada com sucesso.')
        return {'agencia': AGENCIA, 'numero da conta': numero_da_conta, 'usuario': usuario_filtrado}
    else:
        print('Usuário não encontrado. Fluxo de criação de conta encerrado.')
        return None

def listar_contas(contas):
    
    if contas:
         for conta in contas:
           print(f"""
           Agência: {conta['agencia']}
           Número da conta: {conta['numero da conta']}
           Titular: {conta['usuario']['nome']}
         """)
    else:
        print('sem contas por enquanto')
            


def transacoes_financeiras(operacao, saldo, limite, extrato, numero_de_saques, LIMITE_SAQUE, usuarios, contas, numero_da_conta):
    if operacao == 'a':
        valor = float(input('Informe o valor do depósito?\n'))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif operacao == 'b':
        valor = float(input('Quanto você quer sacar?\n'))
        saldo, extrato, numero_de_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_de_saques=numero_de_saques, LIMITE_SAQUE=LIMITE_SAQUE)
    elif operacao == 'c':
        mostrar_extrato(saldo, extrato=extrato)
    elif operacao == 'nu':
        criar_usuario(usuarios)
    elif operacao == 'nc':
        numero_da_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_da_conta, usuarios)
        if conta:
            contas.append(conta)
    elif operacao == 'lc':
        listar_contas(contas)
    elif operacao == 'd':
        print('Saindo...')
        return False, saldo, limite, extrato, numero_de_saques, LIMITE_SAQUE, usuarios, contas, numero_da_conta
    else:
        print('Opção inválida!')
    return True, saldo, limite, extrato, numero_de_saques, LIMITE_SAQUE, usuarios, contas, numero_da_conta

while True:
    opcao = input(menu)
    continuar, saldo, limite, extrato, numero_de_saques, LIMITE_SAQUE, usuarios, contas, numero_da_conta = transacoes_financeiras(opcao, saldo, limite, extrato, numero_de_saques, LIMITE_SAQUE, usuarios, contas, numero_da_conta)
    if not continuar:
        break
 