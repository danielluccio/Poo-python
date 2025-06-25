class Aluno:
    def __init__(self, altura, idade):
        self.altura = altura
        self.idade = idade

    def correr(self) -> bool:
        try:
            if self.idade > 4:
                    print("O muleke está correndo !!")
                    return True
            
        except Exception as e:
            print("Digite um valor inteiro !")
    
        print('O muleke não está correndo !!!')
        return False
        
    def comer(self, fome) -> str:
        if fome == 'fome':
            return "O muleke vai comer"
        else:
            self.correr()


aluno_1 = Aluno(1.30, 'daniel')
print(aluno_1.comer('sem fome'))


    
