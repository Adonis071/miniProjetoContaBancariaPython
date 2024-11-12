from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)    

class pessoa_fisica(Cliente):

    def __init__(self, nome, data_de_nascimento, cpf):
        super().__init__(endereco)        
        self._nome = nome
        self._data_de_nascimento = data_de_nascimento
        self._cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = historico()
     
    @classmethod 
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo  

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente 

    @property
    def historico(self):
        return self._historico                 

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
           print('A operação falhou! Você não tem saldo suficiente.')
        elif valor > 0:
           self._saldo -= valor
           print(f'Saque de R$ {valor:.2f} Reais realizado com sucesso.')
           print('-' * 40)
           return True
        else:
           print('A operação falhou! Valor informado inválido.')
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo +=valor 
            print(f'Depósito de {valor:.2f} realizado com sucesso')  
        else:
            print('A operação falhou tente novamente.')  
            return False
       
        return True     

class Conta_corrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_de_saque = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saque = numero_de_saque > limite_saque

        if excedeu_limite:
            print('A operação falhou você excedeu limite.')
       
        elif excedeu_saque:
            print('A operação falhou você excedeu o limite de saques.')
       
        else:
            return super().sacar(valor)

        return False 

        def __str__(self):
            return f'Agencia: {self.agencia}.\nConta: {self.numero_da_conta}.\nTitular: {self.Cliente.nome}.'


class Historico:
        def __init__(self):
            self._transacoes = []

        @property
        def transacoes(self):
            return self._transacoes    

        def adicionar_transacao(self, transacao):
            self._transacoes.append(
                {
                    'tipo': transacao.__class__.__name__,
                    'valor': transacao.valor,
                    'data': datetime.now().strftime('%d/%m/%Y  %H:%M:%s')
                }
                
                )           

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self) 

class depositar(self, valor):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)                   


