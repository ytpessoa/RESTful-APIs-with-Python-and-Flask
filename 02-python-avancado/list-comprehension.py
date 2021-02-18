

def compreensaoLista():    
    lc= [ x for x in range(5) ]
    lc2=[ x**2 for x in range(5)]
    lc3=[x+10 for x in range(5)]
    print( lc )
    print(lc2)
    print(lc3)
    print('#######')

def teste():
    x=list(range(0,10,2))
    print(x)
    print(type(x))

def pegarPares():
    lc = [ n for n in range(11) if n % 2 == 0  ]
    print(lc)

def normalizando():
    pessoas = [' AnA', 'manuela', 'FELIpe', 'PedrO']
    print(pessoas)
    print("Normalizadas:")
    pessoasNormalizadas = [ p.strip().capitalize() for p in pessoas ]
    print(pessoasNormalizadas)

if __name__ == "__main__":
    #compreensaoLista()
    #teste()
    #pegarPares()
    #normalizando()