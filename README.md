# Projeto: Sistema de Transações Financeiras

## Descrição do Projeto
Este projeto é um sistema simples de transações financeiras em Python, permitindo depósitos, saques e a exibição de extratos. O sistema garante que as regras de negócio, como limites de saque e número máximo de saques, sejam seguidas.

## Funcionalidades
- **Depósito**: Adiciona um valor ao saldo e registra a transação no extrato.
- **Saque**: Verifica o saldo, limite e número de saques antes de deduzir o valor do saldo e registrar a transação no extrato.
- **Extrato**: Exibe todas as transações realizadas e o saldo atual.
- **Sair**: Encerra o programa.

## Implementação
```python
# Menu de opções para o usuário
menu = """
Escolha uma das opções:
[a] Depositar.
[b] Sacar.
[c] Extrato.
[d] Sair.
"""

# Inicialização das variáveis
saldo = 0 
limite = 500
extrato = ''
numero_de_saques = 0
LIMITE_SAQUE = 3

# Função para realizar transações financeiras
def transacoes_financeiras(operacao):
    global limite, LIMITE_SAQUE, saldo, numero_de_saques, extrato
    
    if operacao == 'a':
        # Solicita o valor do depósito
        valor = float(input('Informe o valor do depósito?\n')) 

        if valor > 0:
            saldo += valor
            extrato += f'Depósito de R$ {valor:.2f}\n'
        else:
            print('Valor inválido.')
    
    elif operacao == 'b':
        # Solicita o valor do saque
        valor = float(input('Quanto você quer sacar?\n'))

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
            numero_de_saques += 1
        else:
            print('A operação falhou! Valor informado inválido.')
    
    elif operacao == 'c':
        # Exibe o extrato das transações
        print('\n=============== EXTRATO ===============')
        print('Não foram realizadas transações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('========================================')
    
    elif operacao == 'd':
        # Encerra o loop retornando False
        return False
    
    else:
        print('Opção inválida!')
    
    # Retorna True para continuar o loop
    return True

# Loop principal do programa
while True:
    opcao = input(menu)
    if not transacoes_financeiras(opcao):
        break
