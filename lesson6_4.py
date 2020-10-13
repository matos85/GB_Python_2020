class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул на {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name}: {self.speed}')


class TownCar(Car):
    def __init__(self, name, speed, color, is_police):
        super(TownCar, self).__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed <= 60:
            print(f'Скорость машины: {self.speed}')
        else:
            print(f'Скорость машины: {self.speed}. Внимание! Превышение скорости!')


class SportCar(Car):
    def __init__(self, name, speed, color, is_police):
         super(SportCar, self).__init__(name, speed, color, is_police)


class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
         super(WorkCar, self).__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed <= 40:
            print(f'Скорость машины: {self.speed}')
        else:
            print('Внимание! Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police):
         super(PoliceCar, self).__init__(name, speed, color, is_police)


town_auto = TownCar('Nissan', 80, 'белый', False)
sport_auto = SportCar('Ferrari', 180, 'красный', False)
work_auto = WorkCar('Toyota', 40, 'черный', False)
police_auto = PoliceCar('Chevrolet', 80, 'белый-синий', True)

print('-------town_auto--------')

town_auto.go()
town_auto.show_speed()
town_auto.turn('лево')
town_auto.stop()

print(town_auto.name)
print(town_auto.color)
print(town_auto.speed)
print(town_auto.is_police)

print('-------sport_auto--------')

sport_auto.go()
sport_auto.show_speed()
sport_auto.turn('право')
sport_auto.stop()

print(sport_auto.name)
print(sport_auto.color)
print(sport_auto.speed)
print(sport_auto.is_police)

print('-------work_auto------')

work_auto.go()
work_auto.show_speed()
work_auto.turn('лево')
work_auto.stop()

print(work_auto.name)
print(work_auto.color)
print(work_auto.speed)
print(work_auto.is_police)

print('-----police_auto--------')

police_auto.go()
police_auto.show_speed()
police_auto.turn('право')
police_auto.stop()

print(police_auto.name)
print(police_auto.color)
print(police_auto.speed)
print(police_auto.is_police)
