class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self._titular = titular  # Atributo protegido
        self._saldo = saldo      # Atributo protegido

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'Depósito de {valor} realizado. Novo saldo: {self._saldo}')
        else:
            print('Valor inválido para depósito.')

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f'Saque de {valor} realizado. Novo saldo: {self._saldo}')
        else:
            print('Saldo insuficiente ou valor inválido para saque.')

    def obter_saldo(self):
        return self._saldo

    def obter_titular(self):
        return self._titular


# Criando uma instância da classe ContaBancaria
minha_conta = ContaBancaria('João', 200)

# Tentando acessar diretamente um atributo privado (gerará um erro)
print(minha_conta._saldo)

# Acessando os membros da classe por meio de métodos públicos
minha_conta.depositar(100)
minha_conta.sacar(30)
print(f'Saldo atual: {minha_conta.obter_saldo()}')
print(f'Titular da conta: {minha_conta.obter_titular()}')
