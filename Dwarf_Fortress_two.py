import random


class Dwarf:  # дварф
    def __init__(
        self, Dwarf_name, Dwarf_health_points, Dwarf_speed, Dwarf_weapon, Dwarf_workId
    ):
        self.name = Dwarf_name  # имя
        self.health_points = Dwarf_health_points  # очки здоровья
        self.speed = Dwarf_speed  # скорость
        self.weapon = Dwarf_weapon  # оружее

    def Run(self, new_speed):  # метод изменения скорости
        self.speed = new_speed

    def medicine_chest_plus(self, health_points_plus):  # метод аптечки
        self.health_points += health_points_plus

    def medicine_chest_minus(self, health_points_minus):  # метод урона
        self.health_points -= health_points_minus

    def change_weapons(self):  # смена оружия
        i = random.randint(0, 2)
        wep = ["меч", "лук", "булава"]
        self.weapon = wep[i]


class Weapon:  # оружие
    def __init__(self, Weapon_name, Weapon_cost, Weapon_damage, Weapon_weight):
        self.name = Weapon_name  # имя
        self.cost = Weapon_cost  # стоимость
        self.damage = Weapon_damage  # урон
        self.weight = Weapon_weight  # вес


class Animal:  # животное
    def __init__(
        self,
        Animal_name,
        Animal_health_points,
        Animal_weight,
        Animal_cost,
        Animal_hostility,
    ):
        self.name = Animal_name  # имя
        self.health_points = Animal_health_points  # очки здоровья
        self.weight = Animal_weight  # вес
        self.cost = Animal_cost  # стоимость
        self.hostility = (
            Animal_hostility  # враждебность, 0 - не враждебно, 1 - враждебно
        )

    def weight_loss(self, killogram_squared):  # метод потери веса
        self.weight -= pow(killogram_squared, 2)

    def cost_increase(self, increase):  # метод увеличения стоимости
        self.cost = self.cost * increase

    def become_hostile(self):  # метод превращения в враждебное животное
        self.hostility = 1
        self.cost -= 100


My_Dwarf = Dwarf("Простак", 90, 10, "булава", 0)  # создание обекта класса Dwarf
My_Dwarf.medicine_chest_plus(7)  # срабатывание аптечки
print(My_Dwarf.health_points)
My_Dwarf.medicine_chest_minus(5)  # нанесение урона
print(My_Dwarf.health_points)
My_Dwarf.change_weapons()  # смена оружия
print(My_Dwarf.weapon)

My_Animal = Animal("Alpaca", 50, 5, 1000, 0)  # создание обекта класса Animal
My_Animal.cost_increase(2)  # увеличение стоимости
print(My_Animal.cost)
My_Animal.become_hostile()  # превращение в враждебное животное
print(My_Animal.hostility)
print(My_Animal.cost)
My_Animal.weight_loss(2)  # снижение веса
print(My_Animal.weight)
