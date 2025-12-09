from src.cofre import Cofre
from src.item import Item
from src.moeda import Moeda

if __name__ == '__main__':
    cofre = Cofre(20)
    print(cofre)
    cofre.add(Moeda.M10)
    cofre.add(Moeda.M50)
    print(cofre)

    cofre.add(Item("ouro", 3))
    print(cofre)

    cofre.add(Item("passaporte", 2))
    print(cofre)

    if not cofre.obterItens():
        print("Voce deve quebrar o cofre primeiro")

    if cofre.obterMoedas() == -1:
        print("Voce deve quebrar o cofre primeiro")

    print(cofre)

    cofre.quebrar()
    cofre.quebrar()

    print(cofre.obterItens())
    print(cofre.obterMoedas())
    print(cofre)