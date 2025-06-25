class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    def depositar(self, valor):
        try:
            if valor > 0:
                self.__saldo += valor
                print(f"Seu novo valor de saldo é {self.__saldo}")

            else:
                print("Valor não pode ser nulo")

        except Exception as e:
            print("Digite um valor númerico !!!")



    def sacar(self, valor):
        try:
            if self.__saldo < valor:
                print("Valor de saque maior que o disponivel !!!")

            else:
                self.__saldo -= valor
                print(f"O seu valor de saldo atual: {self.__saldo}")

        except Exception as e:
            print("Digite um valor númerico !!!")


operacao_1 = ContaBancaria(10000)
operacao_1.sacar(2000)
operacao_1.depositar(5000)