

class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    
    def dados(self):
        return {'nome': self.nome, 'salario': self.salario}

class FuncionarioAdmin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def atualizarNome(self, nome):
        self.nome = nome
        return self.dados()


if __name__ == "__main__":
    
    fabio = Funcionario("Fabio", 5000)
    print(fabio.nome)
    print(fabio.salario)
    print(fabio.dados())

    pedro = FuncionarioAdmin("Pedro", 7000)

    print(pedro.dados())

    pedro.atualizarNome("PedroToba")

    print (pedro.dados())