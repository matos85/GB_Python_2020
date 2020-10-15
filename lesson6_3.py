class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super(Position, self).__init__(name, surname, position, wage, bonus)
        self.get_full_name()
        self.get_total_income()

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {self._income["wage"] + self._income["bonus"]}')


workers = Position('Иван', 'Иванов', 'Начальник', 100123, 130123)
