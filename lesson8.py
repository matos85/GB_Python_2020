import random


class LotBilet:
    def __init__(self):
        self.bilet = []
        self.line_1 = []
        self.line_2 = []
        self.line_3 = []
        self.bilet = sorted(random.sample(range(1, 90), k=15))
        self.generate_number()

    def generate_number(self):
        self.line_1 = [i for i in self.bilet[:5]]  # sorted([i for i in self.bilet[:5]])
        self.line_2 = [i for i in self.bilet[5:10]]  # sorted([i for i in self.bilet[5:10]])
        self.line_3 = [i for i in self.bilet[10:]]  # sorted([i for i in self.bilet[10:]])

        for i in range(1, 5):
            self.line_1.insert(random.randint(0, 5), ' ')
            self.line_2.insert(random.randint(0, 5), ' ')
            self.line_3.insert(random.randint(0, 5), ' ')

        self.bilet = self.line_1 + self.line_2 + self.line_3

    def print_bilet(self):
        print('-' * 27)
        print("%3s" * 9 % tuple(self.bilet[0:9]))
        print("%3s" * 9 % tuple(self.bilet[9:18]))
        print("%3s" * 9 % tuple(self.bilet[18:27]))
        print('-' * 27)


class Gamer(LotBilet):
    def __init__(self, name):
        super().__init__()
        self.name = name


class IterB:
    def __init__(self):
        self.numbers = random.sample(range(1, 91), 90)

    def barels(self):
        for i in self.numbers:
            yield i


class Game(IterB, Gamer):
    def __init__(self, player, pc):
        super(Game, self).__init__()
        self.player = player
        self.pc = pc
        self.barell = IterB()

    def start(self):
        print(f'Да начнется игра между {self.player.name}ом и {self.pc.name}ом. Пусть победит ... кто нибудь! ')
        print(f'Карточка: {self.player.name}а')
        self.player.print_bilet()
        print(f'Карточка: {self.pc.name}а')
        self.pc.print_bilet()
        bar = 0
        for num in self.barell.barels():
            flag = False
            if bar == 91:
                print('END')
                break
            if self.player.bilet.count('x') == 15:
                print(f'Победил: {self.player.name}. Ход номер: {bar} ')
                break
            if self.pc.bilet.count('x') == 15:
                print(f'Победил: {self.pc.name}. Ход номер: {bar} ')
                break
            bar += 1
            print(f'Ход номер: {bar}')
            print(f'Выпал боченок с номером: {num}')
            cross_out = input('Зачеркнуть цифру? Варианты ответа Y или N. Ваш ответ: ').lower()
            if cross_out == 'y':
                for m, n in enumerate(self.player.bilet):
                    if n == num:
                        self.player.bilet[m] = 'x'
                        print(f'В карточке {self.player.name}а есть совпадения с боченком номер: {num}')
                        print(f'{self.player.name} зачеркивает номер: {num}')
                        break
                else:
                    print(f'{self.player.name} проиграл. Обманывать не хорошо')
                    flag = True

            if cross_out == 'n':
                for m, n in enumerate(self.player.bilet):
                    if n == num:
                        print(f'{self.player.name} проиграл. Обманывать не хорошо')
                        flag = True
            else:
                print(f'В карточке {self.player.name}а нет совпадений с боченком номер: {num}')
            if flag:
                break
            print(f'Карточка: {self.player.name}а')
            self.player.generate_number()
            self.player.print_bilet()

            for m, n in enumerate(self.pc.bilet):
                if n == num:
                    self.pc.bilet[m] = 'x'
                    print(f'{self.pc.name} зачеркивает номер: {num}')
            else:
                print(f'В карточке {self.pc.name}а нет совпадений с боченком номер: {num}')
            print(f'Карточка: {self.pc.name}а')
            self.pc.generate_number()
            self.pc.print_bilet()
            print(' ')


gamer = Gamer('Игрок')
comp = Gamer('Компьютер')
game1 = Game(gamer, comp)
game1.start()
