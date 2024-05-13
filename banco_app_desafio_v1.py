from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

# Classes

class Conta:
    def __init__(self,numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

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
    
    def sacar(self, valor): # retornar um boolean - sucesso ou falha
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Valor inválido!")
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self,numero, cliente, limite = 500, limite_saque = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self._limite
        excedeu_saque = numero_saques >= self._limite_saque

        if excedeu_limite:
            print("O Valor excedeu o limite.")
        elif excedeu_saque:
            print("Máximo de saques excedido!")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self) -> str:
        return f"""
                Agência: \t{self._agencia}
                Conta-Corrente:\t{self.numero}
                Titular:\t{self._cliente.nome}

        """

class Historico(Conta):
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-%Y %H:%M:%s")

            }

        )

class Transacao(Historico):
    def __init__(self, saldo, numero, agencia, cliente, historico):
        super().__init__(saldo, numero, agencia, cliente, historico)
    
    @property
    @abstractmethod
    def valolr(self):
        pass

    @classmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

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

class Cliente:
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento