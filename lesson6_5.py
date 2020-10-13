class Stationery:
    def __init__(self):
        self.title = 'базовый'

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
         super(Pen, self).__init__()

    def draw(self, title):
        print(f'Запуск отрисовки {title}')


class Pencil(Stationery):
    def draw(self, title):
        print(f'Запуск отрисовки {title}')


class Handle(Stationery):
    def draw(self, title):
        print(f'Запуск отрисовки {title}')


a_stationery = Stationery()
a_pen = Pen()
a_pencil = Pencil()
a_handle = Handle()

a_stationery.draw()
a_pen.draw('ручка')
a_pencil.draw('карандаш')
a_handle.draw('маркер')
