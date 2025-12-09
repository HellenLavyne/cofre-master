import unittest
from enum import Enum

from src.cofre import Cofre
from src.item import Item
from src.moeda import Moeda


class TestCofre(unittest.TestCase):

    def testMoedas(self):
        self.assertTrue(isinstance(Moeda.M10, Enum), "As moedas devem ser enumeracoes")
        self.assertTrue(isinstance(Moeda.M25, Enum), "As moedas devem ser enumeracoes")
        self.assertTrue(isinstance(Moeda.M50, Enum), "As moedas devem ser enumeracoes")
        self.assertTrue(isinstance(Moeda.M100, Enum), "As moedas devem ser enumeracoes")

    def testInicializacao(self):
        cofre = Cofre(25)
        self.assertEqual(25, cofre.getVolumeMaximo(),
                         "Ao inicializar o volumeMaximo do cofre deve ser igual ao informado no construtor")
        self.assertEqual(0, cofre.getVolume(), "Ao inicializar o volume do cofre deve ser igual ao zero")
        self.assertTrue(cofre.taInteiro(), "Ao criar um cofre, ele deve estar inteiro")

    def testInserirMoedaCofreQuebrado(self):
        cofre = Cofre(25)
        cofre.quebrar()
        self.assertFalse(cofre.add(Moeda.M50), "Nao deve ser possivel adicionar uma moeda em um cofre quebrado")

    def testInserirItemCofreQuebrado(self):
        cofre = Cofre(25)
        cofre.quebrar()
        teste = Item("Item teste", 10)
        self.assertFalse(cofre.add(teste), "Nao deve ser possivel adicionar uma moeda em um cofre quebrado")

    def testInserirItemVolumoso(self):
        cofre = Cofre(25)
        arvore = Item("Arvore", 1000)
        self.assertFalse(cofre.add(arvore), "Nao deve ser possivel adicionar um item com volume maior que o do cofre")

    def testInserirItem(self):
        cofre = Cofre(25)
        passaporte = Item("Passaporte", 5)
        self.assertTrue(cofre.add(passaporte), "Tem espaco sobrando, entao deve ser possivel adicionar o item")
        self.assertEqual(20, cofre.getVolumeRestante(),
                         "Ao adicionar um item, o volume restante do cofre deve ser atualizado")

    def testInserirMoeda(self):
        cofre = Cofre(10)
        self.assertTrue(cofre.add(Moeda.M10), "Tem espaco sobrando, entao deve ser possivel adicionar o item")
        self.assertEqual(9, cofre.getVolumeRestante(),
                         "Ao adicionar uma moeda, o volume restante do cofre deve ser atualizado")

    def testInserirItemEmCofreCheio(self):
        cofre = Cofre(4)
        cofre.add(Moeda.M100)
        passporte = Item("Passaporte", 5)
        self.assertFalse(cofre.add(Moeda.M10), "Nao deve ser possivel adicionar algo em um cofre cheio")
        self.assertFalse(cofre.add(passporte), "Nao deve ser possivel adicionar algo em um cofre cheio")

    def testQuebrar(self):
        cofre = Cofre(25)
        self.assertTrue(cofre.quebrar(), "Deve ser possivel quebrar um cofre inteiro")

    def testQuebrarQuebrado(self):
        cofre = Cofre(25)
        self.assertTrue(cofre.quebrar(), "Deve ser possivel quebrar um cofre inteiro")
        self.assertFalse(cofre.quebrar(), "Nao deve ser possivel quebrar um cofre quebrado")

    def testObterMoedaDeCofreInteiro(self):
        cofre = Cofre(10)
        cofre.add(Moeda.M10)
        self.assertEqual(-1, cofre.obterMoedas(), "Nao deve ser possivel obter moedas de um cofre inteiro (-1)")

    def testObterItemDeCofreInteiro(self):
        cofre = Cofre(10)
        cofre.add(Moeda.M10)
        self.assertIsNone(cofre.obterItens(), "Nao deve ser possivel obter itens de um cofre inteiro (null)")

    def testObterMoedas(self):
        cofre = Cofre(10)
        cofre.add(Moeda.M10)
        cofre.add(Moeda.M100)
        cofre.quebrar()
        self.assertEqual(1.1, cofre.obterMoedas(),
                         "Ao obter as moedas, o cofre deve retornar a some de valores da moedas nele contidas")

    def testObterItems(self):
        cofre = Cofre(10)
        passaporte = Item("Passaporte", 5)
        chave = Item("Chave do carro", 3)
        cofre.add(passaporte)
        cofre.add(chave)
        cofre.quebrar()
        self.assertEqual("Passaporte, Chave do carro", cofre.obterItens(),
                         "Ao obter as moedas, o cofre deve retornar a descricao dos itens nele contidos")

    def testObterCofreVazio(self):
        cofre = Cofre(10)
        cofre.quebrar()
        self.assertEqual(0, cofre.obterMoedas(), "Ao obter as moedas, se o cofre estiver vazio ele deve retornar zero")
        self.assertEqual("vazio", cofre.obterItens(),
                         "Ao obter itens, se cofre estiver vazio ele deve retornar 'vazio'")


if __name__ == '__main__':
    unittest.main()