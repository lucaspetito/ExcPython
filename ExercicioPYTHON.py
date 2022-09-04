# Exercício 1
print("1) ")
print ("Ola mundo")
print("")

#----------------------------------------------------------------
# Exercicio 2
print("2) ")
Num = (float(input("Coloca um número ai = ")))
print("O número informado foi = ", Num)
print("")

#----------------------------------------------------------------
# Exercicio 3
print("3) ")
x = (float(input("Coloca um número ai pra somar = ")))
y = (float(input("Coloca mais um número ai pra somar = ")))
resultado = x + y
print("Foi feita uma soma = " , resultado)
print("")
#----------------------------------------------------------------
# Exercicio 4
print("4) ")
x = (float(input("Coloca um número ai pra somar = ")))
y = (float(input("Coloca um número ai pra somar = ")))
w = (float(input("Coloca um número ai pra somar = ")))
z = (float(input("Coloca um número ai pra somar = ")))
media = (x + y + z + w)/4
print("Resultado da média = ", media)
print("")
#----------------------------------------------------------------
# Exercicio 5
print("5) ")
x = (float(input("Coloque um numero em metros para ser convertido em cm = ")))
cm = x / 100
print("Resultado em CM = ", cm , "cm")
print("")
#----------------------------------------------------------------
# Exercicio 6
print("6) ")
r = (float(input("Digite o raio de um circulo  = ")))
r = (r**2)
area = 3.14 * r
print("Area total do circulo = ", area)
print("")
#----------------------------------------------------------------
# Exercicio 7
print("7) ")
l = (float(input("Digite o lado do quadrado = ")))
a = l*l
print("area quadrado = ",a)
print("area quadrado (dobro) = ",a*2)
#----------------------------------------------------------------
# Exercicio 8
print("8) ")
x = (float(input("Valor ganho, horas trabalhadas = ")))
y = (float(input("Horas que trabalha no mes = ")))
re = x*y
print("total do seu salário no referido mês = " , re)
print("")
#----------------------------------------------------------------
# Exercicio 9
print("9) ")
f = (float(input("Coloque grau firehain (perdão, seu escrever n) = ")))
r = 5*((f-32)/9)
print("Graus convertidos em c° = ", r, "c°")
print("")
#----------------------------------------------------------------
# Exercicio 10
print("10) ")
c = (float(input("Coloque grau celcius = ")))
r = ((c/5)*9)+32
print("Graus convertidos em f° = ", r, "f°")
print("")
#----------------------------------------------------------------
# Exercicio 11
print("11) ")
x = (int(input("Coloca um número ai  = ")))
y = (int(input("Coloca um número ai  = ")))
w = (float(input("Coloca um número ai float= ")))
print("o produto do dobro do primeiro com metade do segundo = " , (2*x) * (y/2))
print("a soma do triplo do primeiro com o terceiro = " , (3*x) + w)
print("o terceiro elevado ao cubo =" , w**3)
print("")
#----------------------------------------------------------------
# Exercicio 12
print("12) ")
a = (float(input("Coloca um tua altura ai = ")))
peso = (72.7*a) - 58
print(" teu peso ideal é = " , peso)
#----------------------------------------------------------------
# Exercicio 13
print("13) ")
sexo = (str(input("Coloca seu sexo/homem(h) e mulher(m) = ")))
a = (float(input("Coloca um tua altura ai = ")))
if  ('h' in sexo) :
    print("Senhor seu peso ideal = " , (72.7 * a) - 58)
if  ('m' in sexo) :
    print("Senhora seu peso ideal = " , (62.1 * a) - 44.7)
print("")
#----------------------------------------------------------------
# Exercicio 14
print("14) ")
print("O valor do meu peixe é 20 conto por kg")
kgpexe = (float(input("kg do peixe = ")))
precopexe = kgpexe * 20
exced = kgpexe - 50
if(kgpexe > 50):
    precopexe += kgpexe*4
    multa = precopexe - (exced*4)
else:
    multa = 0
    precopexe = 20*kgpexe
print("valor a se pago do peixe = ", precopexe)
print("multa = " , multa)
print("excesso do pexe = " , exced)
print(" ")
#----------------------------------------------------------------
# Exercicio 15
print("15) ")
x = (float(input("Valor ganho, horas trabalhadas = ")))
y = (float(input("Horas que trabalha no mes = ")))
re = x*y
print("total do seu salário no referido mês = " , re)
print("")
print("Teu salário bruto = " , re)
inss = (re*8)/100
print (" quanto perdeu pro INSS : " , inss)
sind = (re*5)/100
print (" quanto perdeu pro sindicato :",sind)
ir = (re*11)/100
rliquido = re - sind - inss - ir
print( " quanto se fodeu : ", rliquido)
print("")
#----------------------------------------------------------------
# Exercicio 16
print("16) ")
x = float(input("quantidade em metros pra pintar ? "))
quant = x/3
preco = quant*(80/18)
latas = x/54
print ("preco a ser pago : ",preco, " R$")
print("quantidades de latas pra ser usadas : ",latas)
print("")
#----------------------------------------------------------------
# Exercicio 17
print("17) ")
x = float(input("quantidade em metros pra ? "))
quant= x/6
p1 = quant*(80/18)
p2 = quant*(25/3.6)
latas1 = x/54
latas2 = x/10.8
x = input(print("qual vai usar ? escolhe entre (A), (B) ou (C) "
                "\n A)Latas grandes "
                "\n B)Latas Pequenas "
                "\n C)Todas"))
if (x == 'A'):
    print("quantidades de latas pra usar : ",latas1)
    print ("preco que vai pagar : ",p1, " R$")
elif (x == 'B'):
    print("quantidades de latas pra usar : ",latas2)
    print ("preco que vai pagar : ",p2, " R$")
else:
    print("")
#----------------------------------------------------------------
# Exercicio 18
print("18) ")
x = input("tamanho do aqruivo (em MB) ")
y = input("velocidade do link (em Mbps) ")
re = (x/(y/8))
print ("tempo aproximado = ",re/60)






