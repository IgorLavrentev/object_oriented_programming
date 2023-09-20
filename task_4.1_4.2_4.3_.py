import random 

class transport: # класс транспрта
    def __init__(self, transport_length, transport_width, transport_height, transport_weight):
        self._length = transport_length # длина транспортного средства
        self._width = transport_width # ширина транспортного средства
        self._height = transport_height # высота транспортного средства
        self._weight = transport_weight # масса транспортного средства
    
    def engine(self): # двигатель
        print('JT8D')

    def pr(self, __car_speed): # метод для ad hoc полиморфизма
        print(__car_speed)

    def pr(self, __roll_angle): # метод для ad hoc полиморфизма
        print(__roll_angle)

class rims(): # класс автомобильных дисков
    def __init__(self, r):
        self.radius = r

class car(transport): # класс автомобилей
    def __init__(self, transport_length, transport_width, transport_height, transport_weight, eng_type, s, r):
        super().__init__(transport_length, transport_width, transport_height, transport_weight)
        self.__engine_type = eng_type # 1 -ДВС, 2 - электродвигатель
        self.__car_speed = s # скорость автомобиля
        self.__stopping_distance_coefficient = 0 # коэффициент тормозного пути
        self.__car_rims = rims(r) # диски автомобиля
        self.__car_boost = 'yes' # возможно ли ускорение ('yes' или 'no')

    def engine(self): # двигатель
        print(self.__engine_type)

    def get_car_rims(self): # метод вывода на печать радиуса диска
        print(self.__car_rims.radius)

    def speed(self, __new_speed): # скорость
        self.__car_speed = __new_speed

    def get_car_speed(self): # метод вывода на печать скорости автомобиля
        print(self.__car_speed)

    def driving_style(self,__car_speed):  # стиль вождения
        if 1 < __car_speed < 40:
            return 'Стиль вождения дачный'
        elif 40 <= __car_speed < 90:
            return 'Стиль вождения профессиональный'
        elif 90 <= __car_speed:
            return 'Стиль вождения агрессивный'
        
    def ABS(self, a): # включение антиблокировочной системы, 1 - система включена, 0 - система выключена
        if a == 1:
            self.__stopping_distance_coefficient = 0.7
        elif a == 0:
            self.__stopping_distance_coefficient = 1

class aircraft(transport): # класс самолетов 
    def __init__(self, transport_length, transport_width, transport_height, transport_weight, angle):
        super().__init__(transport_length, transport_width, transport_height, transport_weight)
        self.__roll_angle = angle

    def roll_angle_new(self, new_angle): # угол крена
        self.__roll_angle = new_angle

    def get_roll_angle(self): # метод вывода на печать угла крена
        print(self.__roll_angle)

    def check_roll_angle(self, __roll_angle): # проверка допустимого угла крена 
        if 0 < abs(__roll_angle) < 30:
            return 'Допустимый угол крена'
        else:
            return 'Недопустимый угол крена'
    
    def engine(self): # двигатель
        print(self.__roll_angle)

class spacecraft(): # класс космических аппаратов
    def __init__(self, spacecraft_weight, spacecraft_height_orbit, spacecraft_inclination_orbit):
        self._weight = spacecraft_weight # масса
        self._height_orbit = spacecraft_height_orbit # высота 
        self._inclination_orbit = spacecraft_inclination_orbit # наклонение орбиты

class solar_panels(): # класс солнечных панелей
    def __init__(self, solar_panels_area):
        self.area = solar_panels_area # площадь

class manned_spacecraft(spacecraft): # класс пилотируемых космических аппаратов
    def __init__(self, spacecraft_weight, spacecraft_height_orbit, spacecraft_inclination_orbit, oxygen, manned_spacecraft_area):
        super().__init__(spacecraft_weight, spacecraft_height_orbit, spacecraft_inclination_orbit)
        self.__oxygen_volume = oxygen # содержание кислорода в кабине пилотов
        self.__illuminator = 100 # 100 - илююминаор закрыт, 0 - иллюминатор открыт
        self.spacecraft_solar_panels = 2 * manned_spacecraft_area # площадь солнечных панелей
    
    def get_spacecraft_solar_panels(self): # метод вывода на печать площади солнечных панелей
        print(self.spacecraft_solar_panels)

    def oxygen_supply(self, v): # подача кислорода
        self.__oxygen_volume += v

    def regulation_illuminator(self, __closing_percentage): # регулировка иллюминатора
        self.__illuminator = __closing_percentage

class automatic_spacecraft(spacecraft): # класс автоматических космических аппаратов
    def __init__(self, spacecraft_weight, spacecraft_height_orbit, spacecraft_inclination_orbit):
        super().__init__(spacecraft_weight, spacecraft_height_orbit, spacecraft_inclination_orbit)
        self.__engine_thrust = 50 # тяга двигателя
        self.__battery_charge = 50000 # емкость батареи
    
    def orbit_correction(self, __new_thrust): # коррекция орбиты
        self.__engine_thrust = __new_thrust

    def checking_battery_charge(self): # проверка заряда батареи
        return self.__battery_charge
    
    def transmission_of_telemetry_information(self): # передача телеметрической информации
        self.__battery_charge -= 10

# реализация композиции
My_car = car(1400, 200, 300, 5, 2, 30, 15)
My_car.get_car_rims()
My_car.engine()

My_manned_spacecraft = manned_spacecraft(100, 60, 50, 40, 10)
My_manned_spacecraft.get_spacecraft_solar_panels()

My_transport = transport(100, 50, 60, 50)
My_transport.engine()

My_aircraft = aircraft(100, 60, 50, 40, 5)
My_aircraft.engine()

# работа ad hoc полиморфизма
One_car = car(1400, 100, 100, 1000, 1, 30, 15)
One_aircraft = aircraft(5000, 300, 400, 500, 5)

One_car.pr(5)
One_aircraft.pr(10)

print()
# массив из 500 объектов
M = []
for i in range(500):
    x =random.randint(0,1)
    if x == 0:
        M.append(aircraft(5000, 500, 600, 7000, 7))
    else:
        M.append(car(1000, 200, 300, 2000, 1, 3 , 15))
# применение метода 'engine' к каждому элементу массва
for j in range(500):
    M[i].engine()