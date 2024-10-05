menu = """

     'Escolha uma das opções.'

     [a] Depositar.
     [b] Sacar.
     [c] Extrato.
     [d] Sair.

     """

saldo = 0 
limite = 500
extrato = ''
numero_de_saques = 0
LIMITE_SAQUE = 3


def transacoes_financeiras(operacao):
  global limite, LIMITE_SAQUE, saldo, numero_de_saques, extrato

  if operacao == 'a':

        valor = float(input('Informe o valor do depósito?\n')) 

        if valor > 0:
             saldo += valor
             extrato += f'Depósito de R$ {valor:.2f}\n'
        else:
              print('Valor inválido.')

         
  elif operacao == 'b':
            valor = float(input('Quanto você quer sacar?\n'))

            excedeu_saldo= valor > saldo
            excedeu_limite = valor > limite 
            excedeu_saques = numero_de_saques >= LIMITE_SAQUE

            if excedeu_saldo:
             print('A operação falhou! você não tem saldo.')
            elif excedeu_limite:
             print('A operação falhou! limite de saque excedido.')
            elif excedeu_saques:
             print('A operação falhou! número máximo de saques excedido.')
            elif valor > 0:

             saldo -= valor
             extrato += f'Saque no valor de R$ {valor:.2f}\n'
             numero_de_saques +=1
            else:
             print('A operação falhou valor informado inválido.')

  elif operacao == 'c':
           print('\n===============EXTRATO===============')
           print( 'Não foram realizadas transações.' if not extrato else extrato)
           print(f'Saldo R$ {saldo:.2f}')
           print('\n=====================================')

  elif operacao == 'd':
       return False

  else:
        print('Opção inválida!')

  return True     

   
while True:
 opcao = input(menu)
 if not transacoes_financeiras(opcao):
    break

