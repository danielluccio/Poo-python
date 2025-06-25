import time

class SistemaCadastro:


    def cadastro(self, nome, idade):
        if isinstance(nome, str) and (idade, int):
            print("Acessando o banco de dados...")
            time.sleep(3)
            print(f"Nome: {nome}\nIdade: {idade}")      

        else:
            print("Dados Inválidos")  


user_1 = SistemaCadastro()
user_1.cadastro("Daniel Lucio", 19)