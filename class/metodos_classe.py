class MinhaClasse:

    valor_estatico = "Valor fora do construtor"


    def __init__(self, entrada):
        self.entrada = entrada


    # O self percorre toda a class ou (espelha) e ai sim possui acesso a variável estática
    def print_valor_estatico(self):
        print(self.valor_estatico)

    # Quando a função é chamada, o valor é alterado apenas dentro da função !
    def print_valor_alterado(self):
        self.valor_estatico = "Valor alterado do valor estático"
        print(self.valor_estatico)

    
    @classmethod
    def alterando_varial_na_classe_toda(cls):
        cls.valor_estatico = "Valor alterado para todos"

def separador():
    print("*" * 60)
    print("Valor da variável alterado com o decoarador".center(30))
    print("*" * 60)

objeto = MinhaClasse(1)
objeto_2 = MinhaClasse(2)


print(objeto.valor_estatico)
objeto.print_valor_estatico()
objeto.print_valor_alterado()

separador()


objeto_2.alterando_varial_na_classe_toda()
print(objeto_2.valor_estatico)
objeto_2.print_valor_estatico()
objeto_2.print_valor_alterado()