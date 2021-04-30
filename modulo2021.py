import math

def resuelve_desafio(cadena):

    entero = int(cadena)
    sumador = entero % 2021
    multiplcador = (pow(10,len(cadena)) % 2021)
    resultado = 0
    es_numero_grande = entero > 2022
    rango = entero

    if es_numero_grande: rango = 2022
            
    posibles_resultados = []
    
    for i in range(rango):
        resultado = (resultado * multiplcador + sumador) % 2021
        if es_numero_grande: posibles_resultados.append(resultado)
    
    if es_numero_grande: return busca_resultado(posibles_resultados, cadena)
        
    print("-----------")
    
    return print(cadena + ":" + str(resultado))


def busca_resultado(posibles_resultados, entero):

    segmento=[]
    comineza_segmento=0
    
    for i in range(len(posibles_resultados)):

        if posibles_resultados[i] in segmento:
            
            comineza_segmento = i
            break

        segmento.append(posibles_resultados[i])
    
    nuevo_entero = int(entero) - comineza_segmento
    indice = (nuevo_entero % (len(segmento))) - 1

    if indice < 0: indice == len(segmento) - 1
    
    print("-----------")
    
    resultado = (posibles_resultados[indice])

    return print(entero + ":" + str(resultado))


arreglo=["1", "2", "5", "10", "20", "67489454811002199"]

for cadena in arreglo:
    
    resuelve_desafio(cadena)

print("-----------")