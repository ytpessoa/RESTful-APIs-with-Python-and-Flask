


def meuDicionario1():
    meu_dic = { 'nome': 'Ana', 'idade':80 }
    print( meu_dic['nome'] )
    print( meu_dic['idade'] )

def dicionario02():
    loteria = { 'nome': 'Fulano', 'numeros':(13,4,53,67,82) }
    print(loteria)    
    soma = sum(loteria['numeros'])
    print( soma )


if __name__ == "__main__":
    #meuDicionario1()
    dicionario02()
    