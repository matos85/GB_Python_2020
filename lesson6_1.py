import time as t
from itertools import cycle, count


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def __init__(self):
        self.running()

    def running(self):
        # для изменения количеста циклов работы светофора увелить i или удалить/коментировать строки 16,17
        for i in count():
            if i == 3:
                break
            print(self.__color[0])
            t.sleep(7)
            print(self.__color[1])
            t.sleep(2)
            print(self.__color[2])
            t.sleep(7)


light_signal = TrafficLight
#print(light_signal._TrafficLight__color)
light_signal()
