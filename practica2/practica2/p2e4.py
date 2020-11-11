# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#ejercicio 4

#Calcular mayor de los dos numeros

print("Vamos a comprobar cual de los dos numeros es mayor")

numero1 = int(input("introduce por favor el primer numero: "))

numero2 = int(input("introduce por favor el segundo numero: "))

if numero1>numero2:
    
    print("numero '{0}' es mayor que numero '{1}' ".format(numero1,numero2))
    
elif numero1<numero2:
    
    print("numero '{1}' es mayor que numero '{0}' ".format(numero1,numero2))
else:
    
    print("Has indroducido numeros iguales!")
    
print("gracias y adios!")
        
    