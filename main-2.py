import random
import time
palabras= ["desastre","solucionar","aguantar","elefante","celestial","viernes","enero","ordenador","vestido","botella","asteroide","silla","cantante","bondadoso","sensacional","todoterreno","vegetal","soldado","investigador","ornitorrinco"]
palabra =random.choice(palabras)

nombre=input("Hola, bienvenido,¿cómo te llamas?")
print("Hola, "+nombre," vamos a jugar")

time.sleep(1)
print("Tienes que decir una letra para adivinar una palabra aleatoria. Tienes 6 vidas. Así que... comience el juego!")
time.sleep(2)
print("(Tienes que escribir todas las letras en minúsculas)")
tupalabra=" "
vidas=6

while vidas > 0:
    equivocación=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("*",end="")
            equivocación+=1
    if equivocación==0:
        input()
        print("")
        print("felicidades, ganaste")
        input()
        break

    tuletra=input("introduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("fallo")
        print("te quedan ",+vidas," vidas")
    if vidas== 0:
        print("lo siento, has perdido")

        print("Fin del juego.Gracias por participar")

