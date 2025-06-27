class MinhaClasse:

    #Variavel estática, embora se tenha mais objetos da classe, o valor da variável será a mesma !!!
    estatico = 'lhama'

    def __init__(self, estado) -> None:
        self.estado = estado

obj = MinhaClasse(True)
obj_1 = MinhaClasse(True)
MinhaClasse.estatico = "Olá Mundo !!"


print(obj.estatico)
print(obj_1.estatico)







