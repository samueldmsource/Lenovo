import math

kmPercorrido = float(input("Digite a quantidade de km percorrido: "))

combustivelConsumo = float(input("Digite a quantidade de combustivel consumido: "))

ConsumoKmLitro = kmPercorrido / combustivelConsumo

print("Seu veículo faz ", round(ConsumoKmLitro, 3),"km por litro de combustivel")