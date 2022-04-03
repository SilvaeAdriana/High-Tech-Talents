# Enunciado do exercício:

#Fazer a herança das seguintes classes:
#MeioTransporte
#Terrestre            / Aquatico           / Aereo
#Carro / Caminhao     Remo / Barco       Avião / Helicóptero
#Use a imaginação para criar e separar os seus atributos
#Para o dia 07/04


class Transportes():
    nome = ""
    registro = ""
    porte = ""
    passageiros = ""

    def setnome(self, nome):
      Transportes.nome = nome

    def getnome(self):
      return Transportes.nome

    def setregistro(self, registro):
      Transportes.registro = registro

    def getregistro(self):
      return Transportes.registro

    def setporte(self, porte):
      Transportes.porte = porte

    def getporte(self):
      return Transportes.porte

    def setpassageiros(self, passageiros):
      Transportes.passageiros = passageiros

    def getpassageiros(self):
      return Transportes.passageiros

class Terrestre(Transportes):
    combustivel = ""
    numero_rodas = ""
    placa = ""
    numero_portas = ""

class Aquatico(Transportes):
    placa = ""
    forca_motora = ""
    

class Aereo(Transportes):
    numero_helices = ""
    


carro = Terrestre()
carro.setnome('carro')
carro.setpassageiros('4')
carro.setporte('pequeno')
carro.setregistro('2b2b') # chama como função pq tá na classe mãe
carro.combustivel= 'híbrido' # atribuição , parâmetro classe filha
# o erro que dá se chamar/atribuir como acima: TypeError: 'str' object is not callable
carro.numero_rodas = '4'
carro.placa = 'abcde'
carro.numero_portas = '4'




caminhao = Terrestre()
caminhao.setnome('caminhao')
caminhao.setpassageiros('2')
caminhao.setporte('grande')
caminhao.setregistro('2b2b')
caminhao.numero_portas = '2'
caminhao.numero_rodas = '4'
caminhao.placa = 'fghi'
caminhao.combustivel = 'diesel'

remo = Aquatico()
remo.setnome('remo')
remo.setpassageiros('1')
remo.setporte('pequeno')
remo.setregistro('aaa')
remo.forca_motora = 'humana'
remo.placa = 'não tem'


barco = Aquatico()
barco.setnome('barco')
barco.setpassageiros('10')
barco.setporte('médio')
barco.setregistro('bbb')
barco.forca_motora = 'motor'
barco.placa = 'xbxb55'

aviao = Aereo()
aviao.setnome('aviao')
aviao.setpassageiros('40')
aviao.setporte('grande')
aviao.setregistro('sidfj')
aviao.numero_helices = '1'

helicoptero = Aereo()
helicoptero.setnome('helicoptero')
helicoptero.setpassageiros('4')
helicoptero.setporte('pequeno')
helicoptero.setregistro('sggfj')
helicoptero.numero_helices = '2'


print(f' Registro do helicóptero: {helicoptero.getregistro()}')
print(f'Número de passageiros do helicóptero: {helicoptero.getpassageiros()}')





print(dir(Transportes()))
    
    