class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 130156, "bonus": 100000}


class Position(Worker):
    def __init__(self, name, surname, position):
        super(Position, self).__init__(name, surname, position)
        self.get_full_name()
        self.get_total_income()

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {self._income["wage"] + self._income["bonus"]}')


workers = Position('Иван', 'Иванов', 'Начальник')
