class transport: # класс транспрта
    def __init__(self, transport_length, transport_width, transport_height, transport_weight):
        self.__length = transport_length # длина транспортного средства
        self.__width = transport_width # ширина транспортного средства
        self.__height = transport_height # высота транспортного средства
        self.__weight = transport_weight # масса транспортного средства

class car(transport): # класс автомобилей
    def __init__(self, transport_length, transport_width, transport_height, transport_weight, eng_type, s):
        super().__init__(transport_length, transport_width, transport_height, transport_weight)
        self.__engine_type = eng_type # 1 -ДВС, 2 - электродвигатель
        self.__car_speed = s
        self.__stopping_distance_coefficient = 0 # коэффициент тормозного пути
    
    def speed(self, __new_speed): # скорость
        self.__car_speed = __new_speed

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

    def roll_angle_new(self, __new_angle): # угол крена
        self.__roll_angle = __new_angle

    def check_roll_angle(self, __roll_angle): # проверка допустимого угла крена 
        if 0 < abs(__roll_angle) < 30:
            return 'Допустимый угол крена'
        else:
            return 'Недопустимый угол крена'

class spacecraft(): # класс космических аппаратов
    def __init__(self, spacecraft_weight, spacecraft_height_orbit, spacecraft_inclination_orbit):
        self.__weight = spacecraft_weight # масса
        self.__height_orbit = spacecraft_height_orbit # высота 
        self.__inclination_orbit = spacecraft_inclination_orbit

class manned_spacecraft(spacecraft): # класс пилотируемых космических аппаратов
    def __init__(self, spacecraft_weight, spacecraft_height_orbit, spacecraft_inclination_orbit, oxygen):
        super().__init__(spacecraft_weight, spacecraft_height_orbit, spacecraft_inclination_orbit)
        self.__oxygen_volume = oxygen # содержание кислорода в кабине пилотов
        self.__illuminator = 100 # 100 - илююминаор закрыт, 0 - иллюминатор открыт

    def oxygen_supply(self, v): # подача кислорода
        self.__oxygen_volume += v

    def regulation_illuminator(self, __closing_percentage): # регулировка иллюминатора
        self.__illuminator = __closing_percentage

class automatic_spacecraft(spacecraft): # класс автоматических космических аппаратов
    def __init__(self, spacecraft_weight, spacecraft_height_orbit, spacecraft_inclination_orbit):
        super().__init__(spacecraft_weight, spacecraft_height_orbit, spacecraft_inclination_orbit)
        self.__engine_thrust = 50 # тяга двигателя
        self.__battery_charge = 50000
    
    def orbit_correction(self, __new_thrust): # коррекция орбиты
        self.__engine_thrust = __new_thrust

    def checking_battery_charge(self): # проверка заряда батареи
        return self.__battery_charge
    
    def transmission_of_telemetry_information(self): # передача телеметрической информации
        self.__battery_charge -= 10
    