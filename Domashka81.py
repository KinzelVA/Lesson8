"""Конечно! В вашем коде есть несколько ошибок и недочетов, которые нужно исправить:

1. Метод `__init__` в классах `Fighter` и `Monster` должен быть написан как `__init__`, а не `init`.
2. Условие выбора оружия всегда будет выбирать меч, так как `WeaponType.SWORD` всегда верно. Нужно использовать метод `choice` для случайного выбора оружия.
3. В блоке `if __name__ == "__main__":` есть ошибка в названии функции `__name__`, и оно должно быть написано правильно.

Вот исправленный код:"""


from abc import ABC, abstractmethod
from enum import Enum
from random import choice

class WeaponType(Enum):
    SWORD = 1
    BOW = 2

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

class Fighter:
    def __init__(self):
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon is not None:
            return self.weapon.attack()
        else:
            return "У бойца нет оружия!"

class Monster:
    def __init__(self):
        self.health = 10

    def takeDamage(self, damage):
        self.health -= damage

    def isAlive(self):
        return self.health > 0

def main():
    fighter = Fighter()
    monster = Monster()

    # Случайный выбор оружия для бойца
    weapon_choice = choice([WeaponType.SWORD, WeaponType.BOW])
    if weapon_choice == WeaponType.SWORD:
        fighter.changeWeapon(Sword())
    elif weapon_choice == WeaponType.BOW:
        fighter.changeWeapon(Bow())

    attack_result = fighter.attack()
    print(attack_result)

    monster.takeDamage(5)
    if not monster.isAlive():
        print("Монстр побежден!")
    else:
        print(f"У монстра осталось {monster.health} здоровья.")

if __name__ == "__main__":
    main()


