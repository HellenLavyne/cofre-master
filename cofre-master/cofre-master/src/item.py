class Item:


    def __init__(self, descricao: str, volume: int):
        self._volume = volume
        self._descricao = descricao

    def getVolume(self):
        return self._volume

    def getDescricao(self):
        return self._descricao

