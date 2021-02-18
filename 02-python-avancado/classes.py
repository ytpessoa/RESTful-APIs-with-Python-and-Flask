

class JogadorLoteria:
    def __init__(self, nome):
        self.nome = nome
        self.numeros = (13,4,52,23,67,82) 
    
    def total(self):
        return sum(self.numeros)



if __name__ == "__main__":

    jogador1 = JogadorLoteria("Ana")
    jogador2 = JogadorLoteria("Ana")

    print(jogador1.nome)
    print(jogador1.numeros)
    print(jogador1.total())

    print( jogador1 == jogador2  ) #False: objetos diferentes