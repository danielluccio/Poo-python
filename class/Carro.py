class Carro:
    def __init__(self, modelo:str, ano:int, velocidade: float) -> None:
        self.modelo  = modelo
        self.ano = ano
        self.__velocidade = velocidade

    
    def acelerar(self, pedal:bool, velocidade) -> None:
        if pedal == True:
            self.__velocidade += velocidade
            print("Carro está acelerando !!!")
            print(f"Velocidade atual - {self.__velocidade}")
        
        else:
            print("Carro está com a mesma velocidade !!!")
            print(f"Velocidade Atual {self.__velocidade}")

    
    def frear(self, pedal:bool, velocidade) -> None:
        if pedal == True:
            self.__velocidade -= velocidade
            print("Carro está freando !!!")
            print(f"Velocidade atual - {self.__velocidade}")
        
        else:
            print("Carro está com a mesma velocidade !!!")
            print(f"Velocidade Atual {self.__velocidade}")

    def mostrar_velocidade(self) -> float:    
        return self.__velocidade
    

carro_1 = Carro("Honda Civic", 2015, 80.00)
carro_1.acelerar(True, 15.00)
carro_1.frear(False, 0)
print(f"Velocimêtro -> {carro_1.mostrar_velocidade()}")