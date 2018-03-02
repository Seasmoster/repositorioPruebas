
longitud = 30000
valores = "ATGCN"
posicion = 0
c =0

cadena1 = ['GATCTATTTATTT','GATCTTTTTATTT','GATCTGTTTATTT','GATCTCTTTATTT']
cadena2 = ['GATCTNTTNTTNT','GATCTNTTNTTNT','GATCTNTTNTTNT','GATCTNTTNTTNT']
cadena3 = ['GATCTATTTATTT','GATCTTTTTATTT','GATCTGTTTATTT','GATCTCTTTATTT']


origen = "AGTTATGAGGATCTATTTATTT"

while c < len(cadena_evaluar):
    if cadena_evaluar[c] in origen:
        posicion = origen.index(cadena_evaluar[c])
        print(posicion)
        c = len(cadena_evaluar)
 

busca_n = origen[posicion:posicion+12]
print(busca_n)






