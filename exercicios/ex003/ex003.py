from rich import print
from rich import inspect

class ContaBancaria:
    """
    Cria uma conta bancaria e permite que faça depositos e saques
    """
    def __init__(self, id, nome, saldo = 0):# Métodoconstrutor
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {id} bancaria  criada com sucesso.Saldo atual R${self.saldo:,.2f}.')

    def __str__(self):#que aparece quando eu mandar imprimir c1
        return f'A conta:{self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo'

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito: R${valor:,.2f} na conta {self.id} autorizado ')
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque NEGADO no valor de R${valor:,.2f} saldo da conta {self.id} saldo insuficiente ')
        else:
            self.saldo -= valor
            print(f'Saque: R${valor:,.2f} na conta {self.id} autorizado ')

c1 = ContaBancaria(4004, 'Washington', 3000)
print(c1.__doc__)
c1.depositar(500)
c1.sacar(5000)
print(c1)

c = ContaBancaria(4004, 'Washington', 3000)
inspect(c)

