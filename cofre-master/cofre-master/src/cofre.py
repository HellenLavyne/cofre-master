from src.item import Item
from src.moeda import Moeda


class Cofre:

    def __init__(self, volumeMaximo: int):
        self.volumeMaximo = volumeMaximo # Volume máximo inalterável
        self.volume = 0 # Volume atual ocupado, inicia em 0
        self.estaInteiro = True # Estado do cofre
        self.moedas = [] # Lista para armazenar objetos Moeda
        self.itens = [] # Lista para armazenar objetos Item

    def getVolume(self):
        return self.volume  # Retorna o volume atual

    def getVolumeMaximo(self):
        return self.volumeMaximo # Retorna o volume máximo

    def getVolumeRestante(self):
        return self.volumeMaximo - self.volume # Volume restante = Máximo - Atual

    def taInteiro(self):
        return self.estaInteiro  # Retorna True se não foi quebrado


    def add(self, objeto):
        if not self.estaInteiro: # Não se pode adicionar em um cofre quebrado
            return False

        volume_a_adicionar = 0 # Identifica e obtém o volume do objeto

        if isinstance(objeto, Moeda):
            volume_a_adicionar = objeto.getVolume() # É uma Moeda, pega o volume dela

        elif isinstance(objeto, Item):
            volume_a_adicionar = objeto.getVolume()  # É um Item, pega o volume dele

        else:
            return False  # Não é um tipo válido de objeto


        if volume_a_adicionar > self.getVolumeRestante():     # O volume do objeto deve caber no volume restante
            return False  # Item muito volumoso ou cofre cheio

        if isinstance(objeto, Moeda):
            self.moedas.append(objeto)
        else:
            self.itens.append(objeto)

        self.volume += volume_a_adicionar
        return True

    def obterItens(self): # Só pode obter itens se estiver quebrado
        if self.estaInteiro:
            return None  # O teste espera None

        if not self.itens:  # Se o cofre está quebrado e não tem itens, retorna "vazio"
            return "vazio"

        descricoes = [item.getDescricao() for item in self.itens]  #obtém as descrições em uma string separada por vírgula e espaço
        string_itens = ", ".join(descricoes)

        volume_itens = sum(item.getVolume() for item in self.itens)
        self.volume -= volume_itens
        self.itens = [] # Esvazia a lista de itens

        return string_itens

    def obterMoedas(self):
        if self.estaInteiro: # Só pode obter moedas se estiver quebrado
            return -1

        valor_total = sum(moeda.getValor() for moeda in self.moedas)

        volume_moedas = sum(moeda.getVolume()for moeda in self.moedas)
        self.volume -= volume_moedas
        self.moedas = []  # Esvazia a lista de moedas

        return valor_total

    def taInteiro(self):
        return self.estaInteiro # Retorna True se não foi quebrado

    def quebrar(self):
        if self.estaInteiro: # Sò pode quebrar uma vez
            self.estaInteiro = False
            return True
        return False # Se já está quebrado, retorna false

    def toString(self):
        estado_str = "inteiro" if self.estaInteiro else "quebrado"
        return f"volume: {self.volume}/{self.volumeMaximo} estado: {estado_str} itens: {len(self.itens)} moedas {len(self.moedas)}"