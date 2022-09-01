from operator import attrgetter
from functools import total_ordering

# listas
idades = [10, 15, 22, 23, 52, 15]
print(type(idades))
print(idades[0])
print(len(idades))
idades.append(19)  # append adiciona UM elemento no FINAL.
print(idades)
idades.remove(15)  # remove faz com que o PRIMEIRO elemento seja removido.
print(idades)
for idade in idades:
    print(idade)

# idades.clear() para limpar toda a lista idades
print(idades)

print(18 in idades)
print(10 in idades)

if 22 in idades:
    idades.remove(22)
print(idades)

idades.insert(0, 20)  # insert faz com que seja possível aficionar, na posição que quisermos, um elemento.
print(idades)

idades.extend([53, 55])  # extend EXTENDE a lista adicionando todos elementos desse interável.
print(idades)

#para saber a idade no ano que vem
idades_ano_que_vem = [idade + 1 for idade in idades]
print(idades_ano_que_vem)


#para saber a idade no ano que vem, utilizando List Comprehension
print([idade + 1 for idade in idades])
print([idade for idade in idades if idade > 20]) #list comprehension

#juntando as duas lists comprehension em uma função e uma list comprehension
def proximo_ano(idade):
    return idade + 1

print([proximo_ano(idade)for idade in idades if idade > 20])

#Objetos próprios

class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'Código {self.codigo} Saldo {self.saldo}'

conta_do_gui = ContaCorrente(52)
conta_do_gui.deposita(15766)
print(conta_do_gui)

conta_da_dani =ContaCorrente(94)

def deposita_para_todas_as_contas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_do_gui, conta_da_dani]
deposita_para_todas_as_contas(contas)
print(contas[0], contas[1])

#Tuplas (são imutáveis) - usado quando a posição daquele dado importa


guilherme = ("Guilherme", 23, 1999)
daniela = ("Daniela", 22, 2000 )
rebeca = (21, "Rebeca", 2001) # maneira ruim pois muda a ordem e pode virar uma bagunça

conta_gui_tupla = (52, 2000)
print(conta_gui_tupla)
def deposita(conta): #variação "funcional" (separando o comportamento dos dados), diferente de POO.
    novo_saldo = conta[1] +100
    codigo = conta[0]
    return (codigo, novo_saldo)
conta_gui_tupla = deposita(conta_gui_tupla)
print(conta_gui_tupla)

#misturando listas com tuplas
usuarios = [guilherme, daniela]
print(usuarios)
usuarios.append(("Rebeca", 21, 2001)) #adicionando através de tuplas

#Herança e polimorfismo
class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'Código {self._codigo} Saldo {self._saldo}'


class ContaComSeguro(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 1

class ContaInvestimento(Conta):
    pass

conta16 = ContaComSeguro(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(2000)
conta17.passa_o_mes()
print(conta17)


#polimorfismo
contass = [conta16, conta17]
for duck in contass:
    duck.passa_o_mes() #duck type
print(duck)


#Igualdade e o __eq__
@total_ordering # para ganharmos critérios de ordenações como "<="
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'Código {self._codigo} Saldo {self._saldo}'

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        else:
            return self._codigo < other._codigo


class ContaMultiploSalario(ContaSalario):
    pass


conta_igual = ContaSalario(10)
conta_igual2 = ContaSalario(10)
print(conta_igual2 == conta_igual)

print(isinstance(ContaCorrente(987), Conta))
print(isinstance(ContaCorrente(290), ContaCorrente))
print(isinstance(ContaComSeguro(45), Conta))

print("-------------------------------------")

#Outras utilidades com listas e sequências
idadess = [23, 45, 65, 21, 12, 45, 61]
print(len(idades)) #última posição é exclusiva
print(range(len(idadess))) #última posição exclusiva

print("-------------------------------------")
for i in range(len(idadess)):
    print(i, idadess[i])
print("-------------------------------------")
print(list(enumerate(idadess))) #enumerate facilita a implementação do código range(len(idadess))
print("-------------------------------------")
for valor in enumerate(idadess):
    print(valor)
print("-------------------------------------")
for indice, idade in enumerate(idadess):
    print(indice, "X", idade)
print("-------------------------------------")
for nome, idadeee, ano in (usuarios): #desempacotando as tuplas
    print(nome,ano)
print("-------------------------------------")
print(sorted(idadess))
print(reversed(idadess)) #Se devolve um interador, coloca-se o list para forçar a geração e mostrar o resultado.
print(list(reversed(idadess)))

print(sorted(idadess, reverse=True))
print(list(reversed(sorted(idadess)))) #lazy

print("-------------------------------------")
print(idadess)
idadess.sort() #relembrando: listas são mutáveis.
print(idadess)

conta_do_guilherme = ContaSalario(89)
conta_do_guilherme.deposita(1000)
conta_da_daniela = ContaSalario(850)
conta_da_daniela.deposita(1500)
conta_da_rebeca = ContaSalario(100)
conta_da_rebeca.deposita(1500)
print("-------------------------------------")
contas_para_ordernar = [conta_da_daniela, conta_do_guilherme, conta_da_rebeca]
for laco in sorted(contas_para_ordernar, key= attrgetter("_saldo", "_codigo")):
    print(laco)

#após adicionar método "lt" na classe ContaSalario:
print(conta_do_guilherme < conta_da_daniela)
for ordena in sorted(contas_para_ordernar):
    print(ordena)

print(conta_do_guilherme <= conta_da_daniela)
