import math
 
cont =0 
list = []

Num = int(input("Numero a validar: "))

if Num < 0:
  print("Digite un numero positivo")
for inteligente in range(1,Num+1):
    if (Num % inteligente) == 0 :
        cont += 1
        list.append(inteligente)

print(list)

if len(list) > 2:
  print("el ",Num,"si es inteligente")
elif len(list) <= 2:
    print("el ",Num,"no es inteligente")


