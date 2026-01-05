from random import *


class Human:
    def __init__(self, name, level, hp, ac, mp, strenght, agility, physique, iq, wisdom, charisma, action, baction):
        self.name = name
        self.level = level
        self.hp = hp
        self.mp = mp
        self.strenght = strenght
        self.agility = agility
        self.iq = iq
        self.mx_hp = hp
        self.physique = physique
        self.wisdom = wisdom
        self.charisma = charisma
        self.ac = ac
        self.action = action
        self.mx_action = action
        self.baction = baction
        self.mx_baction = baction

    def hit(self, target, technique):
        is_hit = 0
        hits = self.roll_d20()
        if technique == 'Точный удар':
            hits = self.roll_d20() + self.roll_d8()
        hits_total = hits + max(self.strenght, self.agility, self.physique, self.wisdom, self.charisma, self.iq)
        if hits_total >= target.ac:
            is_hit = 1
            print(
                f'1d20: {hits}+{max(self.strenght, self.agility, self.physique, self.wisdom, self.charisma, self.iq)}={hits_total}')
            print(f'{self.name} Попал по {target.name}!')
        elif hits_total < target.ac:
            print(
                f'1d20: {hits}+{max(self.strenght, self.agility, self.physique, self.wisdom, self.charisma, self.iq)}={hits + max(self.strenght, self.agility, self.physique, self.wisdom, self.charisma, self.iq)}')
            print(f'{self.name} Не попал по {target.name}...')
        return is_hit

    def make_saveroll(self):
        saveroll = randint(1, 20) + max(self.strenght, self.agility, self.physique, self.wisdom, self.charisma, self.iq)
        return saveroll

    def is_mx_hp(self):
        if self.hp > self.mx_hp:
            self.hp = self.mx_hp
        return self.hp

    def is_alive(self):
        if self.hp > 0:
            print(f'Текущие хиты {self.name}: {self.hp}/{self.mx_hp} --> {self.name} Жив!')
            return True
        else:
            print(f'Текущие хиты {self.name}: {self.hp}/{self.mx_hp} --> {self.name} Погиб!')
            print(f'{self.name}, Покойся с миром...')
            return False

    def roll_d20(self):
        d20 = randint(1, 20)
        return d20

    def roll_d4(self):
        d4 = randint(1, 4)
        return d4

    def roll_d6(self):
        d6 = randint(1, 6)
        return d6

    def roll_d8(self):
        d8 = randint(1, 8)
        return d8

    def roll_d10(self):
        d10 = randint(1, 10)
        return d10

    def roll_d12(self):
        d12 = randint(1, 12)
        return d12
