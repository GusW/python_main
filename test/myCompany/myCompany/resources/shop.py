class Shop():
    def __init__(self, shop_id: id, name: str) -> None:
        self._shop_id = shop_id
        self._name = name

    @classmethod
    def from_db(cls, shop_id: id, name: str) -> None:
        ''' Creates new Shop instance given the received database info '''
        return cls(shop_id, name)

    @property
    def shop_id(self) -> int:
        ''' shop_id getter method '''
        return self._shop_id

    @property
    def name(self) -> str:
        ''' name getter method '''
        return self._name
