##César by Edgar##
from string import ascii_letters

def count():
    ABC=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    cifrado = input("TEXT: ")
    coincidencias = []
    for i in range(len(ABC)):
        coincidencias.append(cifrado.count(ABC[i]))
    print(ABC, len(ABC),"\n")    
    print(coincidencias,"\n")
    print("La letra que más se repite es: ",ABC[coincidencias.index(max(coincidencias))], " con", max(coincidencias), " repeticiones\n" )
    for i in range(27):
        decode(cifrado, i+1)

def decode(cifrado, flag):
    msg = ""
    AB = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    print("con llave",flag) 
    for i in cifrado:
        if i in AB:
            msg += AB[(AB.index(i)-flag)%(len(AB))]
        else:
            msg += i
    print(msg, "Es el mensaje\n")
       

count()
