class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.calculation_mass_asphalt()

    def calculation_mass_asphalt(self):
        res = int((self._width * self._length * 25 * 5)/1000)
        return print(f'Масса асфальта, необходимая для покрытия всего дорожного полотна = {res} тонн')


prospect_street = Road(20, 5000)
#prospect_street.calculation_mass_asphalt()
