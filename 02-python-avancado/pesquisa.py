
def pequisaSequencial(lista, n):    
    x=0
    while x < len(lista):
        print(f"loop {x} ")
        if(lista[x] == n):
            print("achou")
            break
        x +=1

def pequisaSequencial2(lista, n):
    for i in lista:
        if( i == n):
            print("achou")
            break
    else: print("não achou")
    

if __name__ == "__main__":
    #L = [15,7,27,39]
    #p = int(input("Digite numero pra procurar "))
    #pequisaSequencial(L, p)
    #pequisaSequencial2(L,p)
    L= list(range(50,100,10))
    print(L)


