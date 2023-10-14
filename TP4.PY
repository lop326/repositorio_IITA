#EJERCICIO_1: Escriba una función que muestre todos los números primos entre 1 y un número n  que es 
#ingresado por parámetro. 
'''def num_primos(cant):
    for j in range(2,cant):
        if cant%j==0:
            return False
    return True
        
        
limite=int(input("ingrese el limite: "))
print("los primos son: ")
for numero in range(2,limite):
    if num_primos(numero):
        print(numero,end="-")'''

#EJERCICIO_2: Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta 
#que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje 
#avisando que ya se agregó el condimento al sándwich. 

#pimer version:Use un test condicional en el ciclo while para detener la ejecución.
'''def fun_sandw():
    condiment=input("ingresar condimento: ")
    print(f"se agrego {condiment}") 
    t=0
    while t==0:
        print("si desea dejar de agregar, ingrese 'SALIR'")
        resp=(input())
        if resp.upper()=="SALIR":
            return False
        else:
            return True
cond=True            
while cond:
    cond=fun_sandw()'''

#segunda version:Use un test condicional dentro del ciclo para decidir si continuar la ejecución. 
'''def fun_sandw():
    condiment=input("ingresar condimento: ")
    print(f"se agrego {condiment}") 
    t=0
    while t==0:
        print("si desea dejar de agregar, ingrese 'SALIR'")
        resp=(input())
        if resp.upper()=="SALIR":
            return True
        else:
            return False      

while True:
    if fun_sandw():
        print("FIN")
        break'''
#EJERCICIO_3: 
#A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un 
#tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje 
#describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez 
#usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
'''def hacer_remera(medida,impr):
    print("la medida de la remera es:",medida)
    print(f"la remera debera de tener el siguiente mensaje '{impr}'")
tamaño=input("ingresar tamaño de remera: ")
mensaje=input("ingresar mensaje a imprimir: ")
hacer_remera(tamaño,mensaje)
hacer_remera(impr=mensaje,medida=tamaño)'''
#B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por 
#defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los 
#valores por defecto, y la segunda con valores diferentes. 
'''def hacer_remeras(medida,impr):    
    print("la medida de la remera es:",medida)
    print(f"la remera debera de tener el siguiente mensaje '{impr}'")

cant=int(input("ingresar cantidad de remeras: "))
tamaño=input("ingresar tamaño de remera: ")
mensaje=input("ingresar mensaje a imprimir: ")
I=0
while I<cant:
    I+=1
    if I==1:
        hacer_remeras("L","me gusta python")
    else:
         hacer_remeras(tamaño,mensaje)'''
#EJERCICIO_4: Escriba una función fibonacci(n) que devuelva los n primeros numeros 
#de la serie de Fibonacci.
'''def serie_fibonacc(cant):
    NUMERO1=0
    NUMERO2=0
    I=1
    while I<=cant:
        I=I+1
        suma= NUMERO1+NUMERO2
        X=NUMERO1
        NUMERO1=suma
        NUMERO2=X 
        print(suma)
        if suma==0:
            NUMERO2=1
serie_fibonacc(cant=int(input("ingresar cantidad: ")))'''
#EJERCICIO_5: Calculadora más inteligente: Modifique el ejercicio 9 del primer practico para que 
#la calculadora sea capaz de devolver el resultado solamente de una operación especificada por 
#el usuario.
'''def fun_calcul(numero1,numero2,operac):
    if operac==1:
        suma=numero1+numero2
        return suma
    elif operac==2:
        resta=numero1-numero2
        return resta
    elif operac==3:
        producto=numero1*numero2
        return producto
    elif operac==4:
        division=numero1/numero2
        return division
    elif operac==5:
        potencia= numero1**numero2
        return potencia

print("CALCULADORA")
print("cada operacion tiene su numero identificador")
while True:
    print("suma:'1'\nresta:'2'\nmultiplicacion:'3'\ndivision:'4'\npotencia:'5'")
    operacion=int(input("ingrese que operacion desea realizar: "))
    while operacion<1 or operacion>5:
        print("operacion invalida")
        operacion=int(input("ingrese que operacion desea realizar: "))
    num1=float(input("ingresar primer numero: "))
    num2=float(input("ingresar segundo numero: "))
    print("resultado: ",fun_calcul(num1,num2,operacion))
    print("¿desea seguir operando?")
    resp=input("SI/NO: ")
    while resp.upper()!="SI" and resp.upper()!="NO":
        print("respuesta invalida")
        resp=input("SI/NO: ")    
    if resp.upper()=="NO":
        print("FIN")
        break'''

#EJERCICIO_6: Conversión imperial: Desarrollar un programa en Python que pueda convertir 
#gramos a libras, centímetros a pulgadas y kilómetros a millas. El programa debe permitir la 
#conversión en ambos sentidos. 1.60934 Km = 1 milla 0.393701 pulgadas = 1 cm 0.00220462 
#libras = 1 gramo  
'''def ver_uni(unida_ver):
    tupla_unid=("libras","gramos","kilometros","millas","centimetros","pulgadas")        
    for i in tupla_unid:
        if unida_ver==i:
            return False
    return True


def conver(va_trasn,uni_trans):
    if uni_trans=="libras":
        return va_trasn/0.00220462,"gramos"
    
    elif uni_trans=="gramos":
        return va_trasn*0.00220462,"libras"
       
    elif uni_trans=="kilometros":
        return va_trasn/1.60934,"millas"
        
    elif uni_trans=="millas":
        return va_trasn*1.60934,"kilometros"
       
    elif uni_trans=="centimentros":
        return va_trasn*0.393701,"pulgadas"
       
    elif uni_trans=="pulgadas":
        return va_trasn/0.393701,"centimentros"
    else:
        print("no es una unidad")
        
print("CONVERSIONES DISPONIBLES")
print("millas <--> kilometros")
print("centimetros <--> pulgadas")
print("libras <--> gramos")
while True:       
    valor=float(input("ingresar valor a convertir: "))
    unidad=(input("ingresar la unidad: "))
    while True:
        if ver_uni(unidad.lower()):
            unidad=(input("ingresar la unidad: "))
        else:
            break
    resultado,uni_trans2= conver(valor,unidad.lower())   
    print(resultado,uni_trans2)
    print("¿desea dejar el conversor?")
    resp=input("SI/NO: ")
    while resp.upper()!="SI" and resp.upper()!="NO":
        print("RESPUESTA INCORRECTA")
        resp=input("SI/NO: ")
    if resp.upper()=="NO":
        print("FIN DE CONVERSION")
        break'''
        
#EJERCICIO_7: Cuando un año es bisiesto, el mes más corto del año, febrero, tiene 29 días en 
#vez de 28. Esto sucede casi cada 4 años.
#a) Escriba una función que tome un año y diga si es bisiesto o no.  
'''def año_bisiesto(año):
    if año%4==0:
        if año%100==0:
            if año%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False     

while True:
    año_ing=int(input("ingrese un año: "))
    if año_bisiesto(año_ing):
        print(f"{año_ing} es bisiesto")
    else:
        print(f"{año_ing} no es bisiesto")
    resp=input("¿desea ingresar otro año? (SI/NO): ")
    while resp.upper()!="SI" and resp.upper()!="NO":
        print("responda SI o NO")
        resp=input("¿desea ingresar otro año? ")
    if resp.upper()=="NO":
        print("FIN")
        break'''

#b) Modifique su programa para que devuelva todos los años bisiestos entre el año 
#actual y el año pasado a la función como parámetro (este debe ser posterior al año actual).

'''def año_bisiestos(año_inic,año_act):
    for i in range(año_inic+1,año_act):
        if i %4==0:
            if i %100==0:
                if i %400==0:
                    print(f"{i} es bisiesto")
                else:
                    print(f"{i} no es bisiesto")
            else:
                print(f"{i} es bisiesto")
        else:
            print(f"{i} no es bisiesto")
        
año1=int(input("año inicial: "))
año2=int(input("año actual: "))

año_bisiestos(año1,año2)'''


#EJERCICIO_8:Si listamos todos los números naturales menores a 10 que son múltiplos de 3 o 5, 
#obtenemos 3,5,6 y 9. La suma de estos múltiplos es 23. Encuentre la suma de todos los 
#múltiplos de 3 o 5 menores a 1000. 
'''def suma(limite):
    suma=0
    for i in range(1,limite):
        if i%3==0 or i%5==0:
            suma=suma+i
    return suma

num_lim=int(input("ingrese un limite: "))
print(suma(num_lim))'''