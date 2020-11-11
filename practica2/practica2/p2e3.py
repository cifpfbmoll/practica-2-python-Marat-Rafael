# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#ejercicio 3
#Comprobar si es un numero par o no

print("Vamos a comprobar si un numero es par o no")

num=int(input("Dime un numero por favor: "))

if num%2 != 0:

#if (num/2)%1:
    
    print("numero '{0}' es un numero inpar".format(num))
    
else:
    
    print("numero '{0}' es un numero par".format(num))
    