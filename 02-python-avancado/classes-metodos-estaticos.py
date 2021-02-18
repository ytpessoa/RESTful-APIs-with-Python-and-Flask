

class Funcionario():
    
    aumento = 1.04 # 4%
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def dados(self):
        return {'nome': self.nome, 'salario':self.salario}

    def aplicarAumento(self):
        self.salario = self.salario * self.aumento


if __name__ == "__main__":
   fabio = Funcionario("Fabio", 7000)
   print (fabio.dados())
   fabio.aplicarAumento()
   print(fabio.dados())
