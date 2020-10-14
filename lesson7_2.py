from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        self.name = name
        self.v = v

    @property
    def fabric_consumption(self):
        return f'На пошивку пальто от {self.name} требуется {self.v / 6.5 + 0.5:.2f} ткани'


class Suit(Clothes):
    def __init__(self, name, h):
        self.name = name
        self.h = h

    @property
    def fabric_consumption(self):
        return f'На пошивку косюма от {self.name} требуется {2 * self.h + 0.3:.2f} ткани'


smoking = Suit('Smokin',  160)
armani = Coat('A&J', 160 )


print(smoking.fabric_consumption)
print(armani.fabric_consumption)