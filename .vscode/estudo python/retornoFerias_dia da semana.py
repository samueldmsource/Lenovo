#Você terá umas férias maravilhosas que começam no dia 3, quarta-feira. 
# Você retornará das sua férias depois de 137 noites (Uauu!). 
# Escreva um programa que pede o dia do mês e o dia da semana em que você irá viajar e pede ainda o número 
# de dias que você ficará de férias e imprime o dia da semana que você voltará.

#(SEGUNDA IDEIA) O PROGRAMA SÓ FINCIONA CASO SEGUNDA-FEIRA INICIO DAS FERIAS.
dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

dia_mes = int(input("Digite o dia do mês em que iniciará as ferias : "))
dia_semana_viagem = input("Digite o dia da semana que iniciará as ferias ")


num_dias_ferias = int(input("Digite o número de dias que você ficará de férias: "))

indice_inicio = 9
dias_semana.index(dia_semana_viagem)
retorno = (indice_inicio + num_dias_ferias) % 7

print("Você retornará das suas férias em um dia de ", dias_semana[retorno])

while dias_semana[retorno] == 'Segunda':
    print("Dia das ferias liberado para inicio.")
    break

else:

    print("Escolha outro dia da semana para iniciar as ferias.",)
