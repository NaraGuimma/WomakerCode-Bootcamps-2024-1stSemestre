class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # def dirigir(self):
    #     pass

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def dirigir(self):
        return f"Dirigindo o {self.modelo} {self.marca} de cor {self.cor}"

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def dirigir(self):
        return f"Conduzindo a {self.modelo} {self.marca} com {self.cilindrada}cc"

# Criando instâncias de Carro e Moto
meu_carro = Carro("Toyota", "Corolla", "Prata")
minha_moto = Moto("Honda", "CBR", 1000)

# Usando o método dirigir de cada objeto
print(meu_carro.dirigir())  # Saída: Dirigindo o Corolla Toyota de cor Prata
print(minha_moto.dirigir())  # Saída: Conduzindo a CBR Honda com 1000cc
