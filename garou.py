from main import *


class Magician(Human):
    def __init__(self, name, level, hp, ac, mp, strenght, agility, physique, iq, wisdom, charisma, saveroll, action,
                 baction):
        super().__init__(name, level, hp, ac, mp, strenght, agility, physique, iq, wisdom, charisma, action, baction)
        self.saveroll = saveroll
        self.weapons = 'Посох Иссушения'
        self.spells = ['Мистический заряд', 'Руки Хадара', 'Адское возмездие', 'Псевдожизнь', 'Облако кинжалов']
        self.mx_mp = self.mp
        self.start_action = self.action
        self.start_baction = self.baction

    def choice_weapon_or_spell(self) -> int:
        if self.action > 0:
            if self.mp > 0:
                wos = randint(1, 2)
            else:
                wos = 1
            return wos
        else:
            pass

    def choice_spell(self, wos:int) -> int:
        if self.action > 0:
            if wos == 2:
                if self.mp >= 2:
                    total_spell = randint(0, 4)
                    return total_spell
                elif self.mp == 1:
                    total_spell = choice([0, 1, 3])
                    return total_spell
                else:
                    pass
            else:
                pass
        else:
            pass

    def attack(self, wos:int, target:"Human", total_spell:int):
        if self.action > 0:
            if wos == 1:
                print(f'{self.name} использует {self.weapons}')
                if self.hit(target, 0) > 0:
                    damage = self.roll_d12() + self.strenght
                    if target.make_saveroll() < self.saveroll:
                        damage += self.roll_d10()
                    target.hp -= damage
                    print(f'Нанесено урона: {damage}')
                self.action -= 1
            elif wos == 2:
                if total_spell == 0:
                    print(f'{self.name} использует {self.spells[total_spell]}')
                    if self.hit(target, 0) == 1:
                        damage = self.roll_d10() + self.roll_d10() + self.charisma
                        target.hp -= damage
                        print(f'Нанесено урона: {damage}')
                    self.mp -= 1
                    self.action -= 1
                elif total_spell == 1:
                    print(f'{self.name} использует {self.spells[total_spell]}')
                    if target.make_saveroll() < self.saveroll:
                        damage = self.roll_d8() + self.roll_d8() + self.charisma
                        target.hp -= damage
                        print(f'{target.name} не прошёл спасбросок, Нанесено урона: {damage}')
                    else:
                        damage = (self.roll_d8() + self.roll_d8() + self.charisma) // 2
                        target.hp -= damage
                        print(f'{target.name} прошёл спасбросок, Нанесено урона: {damage}')
                    self.mp -= 1
                    self.action -= 1
                elif total_spell == 2:
                    print(f'{self.name} использует {self.spells[total_spell]}')
                    if target.make_saveroll() < self.saveroll:
                        damage = self.roll_d10() + self.roll_d10() + self.roll_d10() + self.charisma
                        target.hp -= damage
                        print(f'{target.name} не прошёл спасбросок, Нанесено урона: {damage}')
                    else:
                        print(f'{target.name} прошёл спасбросок, 0 урона')
                    self.mp -= 2
                    self.action -= 1
                elif total_spell == 3:
                    print(f'{self.name} использует {self.spells[total_spell]}')
                    self.hp += self.roll_d4() + self.roll_d4()
                    self.is_mx_hp()
                    print(f'Исцеление, Текущие хиты Гароу:{self.hp}/{self.mx_hp}')
                    self.action -= 1
                    self.mp -= 1
                elif total_spell == 4:
                    print(f'{self.name} использует {self.spells[total_spell]}')
                    damage = self.roll_d4() + self.roll_d4() + self.roll_d4() + self.roll_d4() + self.roll_d4() + self.charisma
                    target.hp -= damage
                    print(f'Нанесено урона: {damage}')
                    self.action -= 1
                    self.mp -= 2
        else:
            pass

    def block_turn(self, enemy:"Human"):
        if self.is_alive():
            while self.action != 0:
                choice_weapon_2 = self.choice_weapon_or_spell()
                choice_spell_2 = self.choice_spell(choice_weapon_2)
                self.attack(choice_weapon_2, enemy, choice_spell_2)
            self.action = self.start_action
            self.baction = self.start_baction


Garou = Magician('🪄Гароу', 6, 55, 15, 6, 1, 2, 1, 1, 1, 3, 14, 1, 0)
