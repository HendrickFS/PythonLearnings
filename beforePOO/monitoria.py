#Exec 01
def maiorMenor(n1,n2,n3):
    return max(n1,n2,n3)
#Exec 02
def par(n):
    if n%2==0:
        return True
    return False
#Exec 03
def StringMaiuscMinusc(str):
    maiuscula=0
    minuscula=0
    for i in str:
        if i.isupper():
            maiuscula+=1
        elif i.islower():
            minuscula+=1
        else:
            print(i)
    print("Maiusculas:",maiuscula)
    print("Minusculas:",minuscula)

#Exec 04
def todosIguais(x,y,z):
    if x == y and y == z:
        return True
    return False
def todosDiferentes(x,y,z):
    if x != y and y !=z:
        return True
    return False
def ordenados(x,y,z):
    if x < y and y < z:
        return True
    return False
#Exec 05
def geraLista(n,inicio,fim):
    L=[]
    for i in range(n):
        L.append(random.randint(inicio,fim))
    return L
#Exec 06
def numerosUnicos(lista):
    unicos=[]
    for i in lista:
        if not (i in unicos):
            unicos.append(i)
    return unicos
#Exec 07
def palindromo(str):
    str=str.replace(' ','')
    if str==str[::-1]:
        print("eh palindromo")
    else:
        print("nao eh palindromo")

#Exec 08
def corresponde(s1, s2):
    c=0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j] and i == j:
                c+=1
    return c
#Exec 09
def troca(lista):
    trocada=[]
    for i in lista:
        trocada.append(i)

    trocada[0]=lista[-1]
    trocada[-1]=lista[0]
    return trocada
def frente(lista):
    listaNova=[]
    for i in lista:
        listaNova.append(i)

    numero=listaNova[len(lista)-1]
    for i in range(len(lista)-1,0,-1):
        listaNova[i]=listaNova[i-1]
    listaNova[0]=numero
    return 
def achaPares(lista):
    listaNova=[]
    for i in lista:
        listaNova.append(i)

    for i in listaNova:
        if i%2==0:
            i=0
    return listaNova
def indicesPares(lista):
    listaNova=[]
    for i in lista:
        listaNova.append(i)

    for i in range(len(listaNova)-1):
        if i%2==0:
            listaNova[i]=0
    return listaNova
def crescente(lista):
    numero=lista[0]
    for i in lista:
        if i<numero:
            return False
        else:
            numero=i
    return True

#Exec 12
def findAll(str,c):
    lista=[]
    for i in range(0,len(str)):
        if str[i]==c:
            lista.append(i)
    return lista

def isPrimo(n):
    a=n-1
    i=0
    while i<a:
        if a==1:
            return ("É primo")
        elif n%a==0:
            return ("Não é primo")
        else:
            a-=1

def isPrimo2(inicio, fim):
    cont=0
    for i in range(inicio,fim+1):
        divs=0
        for j in range(1,i+1):
            if i%j==0:
                divs+=1
        if divs==2:
            cont+=1
    return cont

def troca(lista):
    numero=lista[0]
    lista[0]=lista[len(lista)-1]
    lista[len(lista)-1]=numero
    return lista

def frente(lista):
    numero=lista[len(lista)-1]
    for i in range(len(lista)-1,0,-1):
        lista[i]=lista[i-1]
    lista[0]=numero
    return lista


def verificaSenha(str):
    if len(str)<10:
        return False
    digitos="0123456789"
    letras="abcdefghijklmnopqrstuvwxyz"
    maiusc=letras.upper()
    numDigitos=0
    numMaiusc=0
    for i in str:
        if not(i in digitos) and not(i in letras) and not(i in maiusc):
            return False
        if i in digitos:
            numDigitos+=1
        if i in maiusc:
            numMaiusc+=1
    if numDigitos<2:
        return False
    if numMaiusc<1:
        return False

    return True

def corresponde(str1,str2):
    correspondencias=0
    for i in range(len(str1)-1):
        for j in range(len(str2)-1):
            if str1[i] == str2[j] and i == j:
                correspondencias+=1

    return correspondencias


def parouimpar(n):
    if (n % 2 == 0):
        return True
    return False

