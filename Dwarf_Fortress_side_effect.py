class Dwarf:  # класс Дварфов
    name = "Простак"  # имя
    age = 35  # возраст
    height = 152  # рост
    speed = 8  # скорость
    weapon = 1  # оружее
    language = "eng"  # язык
    trained_animal = "Alpaca"  # тренируемое животное


class weapon:  # класс оружия
    name = "Baton"  # имя
    cost = 100  # стоимость
    damage = 7  # урон
    weight = 10  # вес


class animals:  # класс животных
    name = "Alpaca"  # имя
    weight = 10  # вес
    cost = 900  # стоимость
    hostility = "no"  # враждебность


# создание объекта класса оружие, поприсваивайте значения его полям
My_weapon = weapon()
My_weapon.name = "spear"
My_weapon.cost = 100
My_weapon.damage = 2
My_weapon.weight = 2
print(My_weapon)


# создание объекта класса животных, поприсваивайте значения его полям
My_animals = animals()
My_animals.name = "Alpaca"
My_animals.weight = 10
My_animals.cost = 900
My_animals.hostility = "no"
print(My_animals)

# создание объекта класса Дварфов, поприсваивайте значения его полям
My_Dwarf = Dwarf()
My_Dwarf.name = "Торин"
My_Dwarf.age = 37
My_Dwarf.height = 160
My_Dwarf.speed = 9
My_Dwarf.weapon = My_weapon
My_Dwarf.language = "ru"
My_Dwarf.trained_animal = My_animals
print(My_Dwarf)

My_Dwarf_number_two = My_Dwarf

My_Dwarf_number_two.age = 41

print(My_Dwarf.age)
