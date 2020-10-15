"""
Distancia 
1 milla = 1.609 km
1 año luz = 9,460,730,472,580.8 km
1 UA (Unidad Atronómica) =  149,597,870,700m

Peso
1 libra = 0.453 kg

Temperatura
Fahrenheit a Celsius
C = (5*(F-32))/9

Celsius a Fahrenheit
F = (9 * C)/5 + 32

Kelvin a Celsius
C = K - 273.15

Celsius a Kelvin
K = C + 273.15

Fahrenheit a Kelvin
K = (5*(F-32))/9 +273.15

Kelvin a Fahrenheit
F = (9*(K -273.15))/5 + 32
"""

def luz_a_km(luz):
    km = luz * 9460730472580.8
    return km
def km_a_luz(km):
    luz = km /9460730472580.8
    return luz

def UA_a_km(UA):
    km = UA *149597870.7
    return km

def km_a_UA(km):
    UA = km/149597870.7
    return UA

def mi_a_km(mi):
    km = mi * 1.609
    return km

def km_a_mi(km):
    mi = km / 1.609
    return mi

def li_a_kg(li):
    kg = li * 0.453
    return kg
def kg_a_li(kg):
    li = kg / 0.453
    return li

def celsius_a_kelvin(C):
    K = C + 273.15
    return K
def kelvin_a_celsius(K):
    C = K - 273.15
    return C
def celsius_a_fahr(C):
    F = (9 * C)/5 + 32
    return F
def fahr_a_celsius(F):
    C = (5*(F-32))/9
    return C
def fahr_a_kelvin(F):
    K = (5*(F-32))/9 +273.15
    return K

def kelvin_a_fahr(K):
    F = (9*(K -273.15))/5 + 32
    return F


if __name__ == "__main__":
    planeta = input("Ingrese el nombre del planeta: ")
    dato = input("Ingrese la distancia del planeta al Sol: ")
    dato = dato.replace(".","")
    dato = float(dato)
    distancia_planetaria = km_a_UA(dato)
    print(f"La distancia de {planeta} en Unidad Astronómica al Sol es: " +str(distancia_planetaria))