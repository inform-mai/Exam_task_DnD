from main import *


class Barbarian(Human):
    def __init__(self, name, level, hp, ac, mp, strenght, agility, physique, iq, wisdom, charisma, action, baction):
        super().__init__(name, level, hp, ac, mp, strenght, agility, physique, iq, wisdom, charisma, action, baction)
        self.weapons = ['Боевой молот', 'Ручные топоры', 'Кинжал']
        self.skills = 'Ярость'
        self.start_action = self.action
        self.start_baction = self.baction
        self.start_strenght = self.strenght

    def choice_weapon(self) -> int:
        if self.action > 0 and self.baction > 0:
            total_weapon = randint(0, 2)
            return total_weapon
        elif self.action > 0 and self.baction == 0:
            total_weapon = randint(0, 1)
            return total_weapon
        elif self.action == 0 and self.baction > 0:
            total_weapon = 2
            return total_weapon
        else:
            pass

    def choice_skills(self):
        if self.baction > 0:
            skill = randint(0, 1)
            if skill:
                print(f'{self.name} В ЯРОСТИ!!!')
                self.strenght += 4
                self.ac -= 2
                self.baction -= 1
            else:
                pass
        else:
            pass

    def attack(self, target:"Human", total_weapon:int):
        if self.action > 0 and self.baction > 0:
            if total_weapon == 0:
                print(f'{self.name} Выбрала {self.weapons[total_weapon]}')
                if self.hit(target, 0) == 1:
                    damage = self.roll_d8() + self.roll_d4() + self.strenght
                    target.hp -= damage
                    print(f'Нанесено {damage} урона!')
                self.action -= 1
            elif total_weapon == 1:
                print(f'{self.name} Выбрала {self.weapons[total_weapon]}')
                if self.hit(target, 0) == 1:
                    damage = self.roll_d6() + self.roll_d6() + self.strenght
                    target.hp -= damage
                    print(f'Нанесено {damage} урона!')
                self.action -= 1
            elif total_weapon == 2:
                print(f'{self.name} Выбрала {self.weapons[total_weapon]}')
                if self.hit(target, 0) == 1:
                    damage = self.roll_d4() + self.strenght
                    target.hp -= damage
                    print(f'Нанесено {damage} урона!')
                self.baction -= 1
        elif self.action > 0 and self.baction == 0:
            if total_weapon == 0:
                print(f'{self.name} Выбрала {self.weapons[total_weapon]}')
                if self.hit(target, 0) == 1:
                    damage = self.roll_d8() + self.roll_d4() + self.strenght
                    target.hp -= damage
                    print(f'Нанесено {damage} урона!')
                self.action -= 1
            elif total_weapon == 1:
                print(f'{self.name} Выбрала {self.weapons[total_weapon]}')
                if self.hit(target, 0) == 1:
                    damage = self.roll_d6() + self.roll_d6() + self.strenght
                    target.hp -= damage
                    print(f'Нанесено {damage} урона!')
                self.action -= 1
            elif total_weapon == 2:
                pass
        elif self.action == 0 and self.baction > 0:
            if total_weapon == 0:
                pass
            elif total_weapon == 1:
                pass
            elif total_weapon == 2:
                print(f'{self.name} Выбрала {self.weapons[total_weapon]}')
                if self.hit(target, 0) == 1:
                    damage = self.roll_d4() + self.strenght
                    target.hp -= damage
                    print(f'Нанесено {damage} урона!')
                self.baction -= 1
        else:
            pass

    def block_turn(self, enemy:"Human"):
        self.ac = 14
        if self.is_alive():
            while self.action > 0 or self.baction > 0:
                choice_weapon_3 = self.choice_weapon()
                self.choice_skills()
                self.attack(enemy, choice_weapon_3)
            self.action = self.start_action
            self.baction = self.start_baction
            self.strenght = self.start_strenght


Vul_Gul = Barbarian('🗡️Вуль гуль', 2, 26, 14, 0, 2, 1, 2, 0, 1, 1, 2, 2)
