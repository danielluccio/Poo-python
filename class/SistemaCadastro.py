import time

class SistemaCadastro:
#SINGLE_RESPOMSABILITY

    def cadastro(self, nome: str, idade: int):
        if self.__validate_input(nome, idade):
            self.__register_user(nome, idade)
        else:
            self.__error_handle()

    
    def __validate_input(self, nome:str, idade: int):
        return isinstance(nome, str) and isinstance(idade, int)
    
    def __register_user(self, nome:str, idade:int) -> None:
        time.sleep(3)
        print("Acessando o Banco de Dados")
        print(f"Nome: {nome}\nIdade: {idade}")  

    def __error_handle(self) -> None:
        print("Dados Inválidos")




