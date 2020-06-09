import math

def desafio(cadena):

    entero=int(cadena)
    sumador= entero%2017
    multiplcador= (pow(10,len(cadena))%2017)
    resto=0
    numeroGrande=(entero>505)
    rango=entero

    if numeroGrande: rango=505
            
    respuestas=[]
    
    for i in range(rango):

        resto=(resto*multiplcador+sumador)%2017
        
        if numeroGrande: respuestas.append(resto)
        
    
    if numeroGrande: return analiza_respuestas(respuestas, cadena)
        
    print("-----------")
    
    return print(cadena + ":" + str(resto))


def analiza_respuestas(respuestas, entero):

    segmento=[]
    corteSegmento=0
    
    for i in range(len(respuestas)):

        if respuestas[i] in segmento:
            
            corteSegmento=i
            break

        segmento.append(respuestas[i])
    
    cortoEntero=int(entero)-corteSegmento
    indice=(cortoEntero%(len(segmento)))-1
    
    print("-----------")
    
    resto=(respuestas[indice])
    return print(entero + ":" + str(resto))


arreglo=["1", "2", "5", "10", "20", "58184241583791680"]

for cadena in arreglo:
    
    desafio(cadena)

print("-----------")