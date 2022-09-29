#EstruturaDeDecisao

#Ex 5

nota1 = float(input("Nota 1 = "))
nota2 = float(input("Nota 2 = "))

med = (nota1 + nota2)/2

def Resultado():
    if (med >= 7.0) and (med < 10.0):
        print("Aprovado")
    else:
        ("Reprovado")
    if (med == 10.0):
        print("Aprovado com distinção")

#Caso eu deseja-se adicionar novos alunos, seria interessante a existencia do método  para não repetir CODE
Resultado()
#------------------------------------------------------------------------------------------------------------
#Ex 7
print("")
numero1 = int(input("Primeiro número :"))
numero2 = int(input("Segundo número :"))
numero3 = int(input("Terceiro número :"))


def Comparar():
    if ((numero1 > numero2) and (numero1 > numero3)):
        print(numero1, " Maior número")
    else:
        print(numero3, " Maior número")
    if ((numero2 > numero1) and (numero2 > numero3)):
        print(numero2, " Maior número")


Comparar()
# ------------------------------------------------------------------------------------------------------------
# Ex 12
print("")
print("Folha de Pagamento \n")
salhr   =     float(input("salário por hora no mês  : "))
hr      =     float(input("horas trabalhadas no mês : "))
Sal = (salhr * hr)
INSS =(Sal*10)/100
IR = (Sal*5)/100
Des = IR + INSS
Salliq = Sal - Des
FGTS = (11*Sal)/100
if (Sal <= 900):
    print("Isento")
    Des = 0
    print(Salliq)
elif((Sal>900)and(Sal<=1500)):
    print("Desconto de 5%")
    print((Sal*5)/100)
    print(Salliq -(Sal*5)/100)
elif((Sal>1500)and(Sal<=2500)):
    print("Desconto de 10%")
    print((Sal*10)/100)
    print(Salliq-(Sal*10)/100)
else:
    print("Desconto de 20%")
    print("Salário Bruto:      : ",Sal)
    print("(-) IR (5%)         : ",IR)
    print("(-) INSS ( 10%)     : ",INSS)
    print("FGTS (11%)          : ",FGTS)
    print("Total de descontos  : ",Des)
    print("Salário Liquido     : ",Salliq)
    print((Sal*20)/100)
#__________________________________________________________________________________________________________
#EstruturaDeDecisao

#Ex 9
print("")
inicio = int(input("Inicio dos numeros imp : "))
fim = int(input("fim dos numeros imp : "))
for num in range(inicio, fim + 1):
    if num % 2 != 0:
        print(num)
#__________________________________________________________________________________________________________
#Ex 12
print("")
numero = int(input ("Digite o número do qual o usuário deseja imprimir a tabuada: "))
print ("Tabela de : ", numero)
for count in range(1, 11):
   print (numero, 'x', count, '=', numero * count)
#__________________________________________________________________________________________________________
#Ex 44
print("")
votacao = T = M = E = J = C = N = B = 0
print('\n---Eleições 2022---\n')
print("\t \t \t Candidatos ! \n [1]Manoel \t [2]Elaine \t [3]Jorge \t [4]Creusa \t [5]Nulo \t [6]Voto em Branco \n")
votacao = int(input("Deseja realizar a votação ? [1] sim \t [0] não \n"))
while votacao != 0:
    voto = int(input(" Digite o número do seu candidato: \n "))
    match voto:
        case [1]:
            print("O Número de Votos em Manoel é igual a : ", M)
            M += M
        case [2]:
            print("O Número de Votos em Elaine é igual a : ", E)
            E += E
        case [3]:
            print("O Número de Votos em Jorge é igual a : ", J)
            J += J
        case [4]:
            print("O Número de Votos em Creusa é igual a : ", C)
            C += C
        case [5]:
            print("O Número de Votos em Nulo é igual a : ", N)
            N += N
        case [6]:
            print("O Número de Votos em Voto em Branco é igual a : ", B)
            B += B
T = T + 1
votacao = int(input("Deseja continuar votando ? \t [1] sim \t [0] não \n"))
PN = N / T
PB = B / T
print("Fim de Votação \n")
print("Resultado da Votação \n")
print("Total de Votos = ", T)
print("Votos em Manoel = ", M)
print("Votos em Elaine = ", E)
print("Votos em Jorge = ", J)
print("Votos em Creusa = ", C)
print("----------------------")
print("Votos Nulo = ", N)
print("Votos em Branco = ", B)
print("porcentagem votos nulos/total = ", PN, "%")
print("porcentagem votos brancos/total = ", PB, "%")


