class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
        # self.nome = nome
        # self.salario = salario

    # def calcular_pagamento(self):
    #     return self.salario        

    def calcular_pagamento(self):
        salario_base = super().calcular_pagamento()
        # salario_base = self.salario
        return salario_base + self.bonus
        
class Secretario(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        # self.nome = nome
        # self.salario = salario

    # def calcular_pagamento(self):
    #     return self.salario        

    # def calcular_pagamento(self):
    #     salario_base = super().calcular_pagamento()
    #     # salario_base = self.salario
    #     return salario_base + self.bonus        


class Programador(Funcionario):
    def __init__(self, nome, salario, horas_trabalhadas, valor_hora):
        super().__init__(nome, salario)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self):
        return self.salario + (self.horas_trabalhadas * self.valor_hora)


gerente = Gerente("João", 5000, 1000)
programador = Programador("Maria", 3000, 160, 20)
secretario = Secretario("Joao", 3000)

print(f"Salário do gerente {gerente.nome}: R$ {gerente.calcular_pagamento()}")
print(f"Salário do programador {programador.nome}: R$ {programador.calcular_pagamento()}")
print(f"Salário do secretario {secretario.nome}: R$ {secretario.calcular_pagamento()}")
