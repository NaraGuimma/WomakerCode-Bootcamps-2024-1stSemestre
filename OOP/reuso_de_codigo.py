class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"{self.modelo} está acelerando.")

    def frear(self):
        print(f"{self.modelo} está freando.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas

    # def acelerar(self):
    #     print(f"{self.modelo} está acelerando.")

    # def frear(self):
    #     print(f"{self.modelo} está freando.")        

    def abrir_porta(self):
        print(f"A porta {self.num_portas} do {self.modelo} foi aberta.")


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
        # self.marca = marca
        # self.modelo = modelo        

    # def acelerar(self):
    #     print(f"{self.modelo} está acelerando.")

    # def frear(self):
    #     print(f"{self.modelo} está freando.")             

    def empinar(self):
        print(f"{self.modelo} está empinando.")

# # Criando uma instância de Carro
# carro = Carro("Toyota", "Corolla", 4)
# print(carro.marca)  # Saída: Toyota
# print(carro.num_portas)  # Saída: 4
# carro.acelerar()  # Saída: Corolla está acelerando.
# carro.frear()
# carro.abrir_porta()

# Criando uma instância de Moto
moto = Moto("Honda", "CBR1000RR", "1000cc")
print(moto.marca)  # Saída: Honda
print(moto.cilindrada)  # Saída: 1000cc
moto.frear()  # Saída: CBR1000RR está freando.
moto.acelerar()  # Saída: Corolla está acelerando.
moto.empinar()
moto.abrir_porta()