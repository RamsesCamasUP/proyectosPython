import random
vidas=0
aleatorio=int(random.random()*10)
contador = 0
while vidas <=3:
    vidas_restantes = 3 - contador
    if vidas ==3:
        print("Has perdido, te quedaste sin vidas")
        break
    numero=int(input(f"Humano que numero entre 1 y 100 crees que estoy pensando ({aleatorio}): "))
    if numero<aleatorio:
        print(f"El numero {numero} es menor al que estoy pensando")
    elif numero>aleatorio:
        print(f"El numero {numero} es mayor al que estoy pensando")
    if numero==aleatorio:
        print(f"FELICIDADES HUMANO LE ATINASTE AL NUMERO MAGICO CON {vidas_restantes} VIDAS RESTANTES")
        break
    contador +=1
    vidas+=1