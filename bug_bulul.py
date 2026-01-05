from main import *


class Bard(Human):
    def __init__(self, name, level, hp, ac, mp, strenght, agility, physique, iq, wisdom, charisma, saveroll, action,
                 baction):
        super().__init__(name, level, hp, ac, mp, strenght, agility, physique, iq, wisdom, charisma, action, baction)
        self.saveroll = saveroll
        self.spells = ['Злая насмешка', 'Лечащее слово', 'Диссонирующий шёпот', 'Разбрасывание карт']
        self.mx_mp = self.mp
        self.start_action = self.action
        self.start_baction = self.baction

    def choice_spell(self) -> int:
        if self.mp >= 0:
            if self.action > 0 and self.baction > 0:
                if self.mp >= 2:
                    total_spell = randint(0, 3)
                    return total_spell
                elif self.mp == 1:
                    total_spell = randint(0, 1)
                    return total_spell
                elif self.mp == 0:
                    total_spell = 0
                    return total_spell
            elif self.action > 0 and self.baction == 0:
                if self.mp >= 2:
                    total_spell = choice([0, 2, 3])
                    return total_spell
                elif 0 <= self.mp <= 1:
                    total_spell = 0
                    return total_spell
            elif self.action == 0 and self.baction > 0:
                if self.mp >= 1:
                    total_spell = 1
                    return total_spell
                else:
                    pass
            elif self.action == 0 and self.baction == 0:
                pass

    def heal(self, target:"Human"):
        heals = self.roll_d4() + 2
        target.hp += heals
        target.is_mx_hp()
        print(
            f'{self.name} восстановил {target.name} {heals} хитов! Текущие хиты {target.name}: {target.hp}/{target.mx_hp}')

    def attack(self, target:"Human", total_spell:int):
        if total_spell == 0:
            print(f'{self.name} Выбрала {self.spells[total_spell]}')
            if target.make_saveroll() < self.saveroll:
                damage = self.roll_d4() + self.roll_d4() + self.charisma
                target.hp -= damage
                print(f'{target.name} не прошёл спасбросок. Нанесено {damage} урона!')
            else:
                print(f'{target.name} прошёл спасбросок. Нанесено 0 урона!')
            self.action -= 1
        elif total_spell == 1:
            print(f'{self.name} Выбрала {self.spells[total_spell]}')
            heal = self.roll_d4() + 2
            self.hp += heal
            self.is_mx_hp()
            print(f'Восстановлено: {heal} хитов. Текущие хиты {self.name}: {self.hp}/{self.mx_hp}')
            self.mp -= 1
            self.baction -= 1
        elif total_spell == 2:
            print(f'{self.name} Выбрала {self.spells[total_spell]}')
            if target.make_saveroll() < self.saveroll:
                damage = self.roll_d6() + self.roll_d6() + self.roll_d6() + self.charisma
                target.hp -= damage
                print(f'{target.name} не прошёл спасбросок. Нанесено {damage} урона!')
            else:
                damage = (self.roll_d6() + self.roll_d6() + self.roll_d6() + self.charisma) // 2
                target.hp -= damage
                print(f'{target.name} прошёл спасбросок. Нанесено {damage} урона!')
            self.mp -= 2
            self.action -= 1
        elif total_spell == 3:
            print(f'{self.name} Выбрала {self.spells[total_spell]}')
            if target.make_saveroll() < self.saveroll:
                damage = self.roll_d10() + self.roll_d10() + self.charisma
                target.hp -= damage
                print(f'{target.name} не прошёл спасбросок. Нанесено {damage} урона!')
            else:
                damage = (self.roll_d10() + self.roll_d10() + self.charisma) // 2
                target.hp -= damage
                print(f'{target.name} прошёл спасбросок. Нанесено {damage} урона!')
            self.mp -= 2
            self.action -= 1

    def block_turn(self, enemy:"Human"):
        if self.is_alive():
            while self.action > 0 or self.baction > 0:
                choice_spell_4 = self.choice_spell()
                self.attack(enemy, choice_spell_4)
            self.action = self.start_action
            self.baction = self.start_baction


Bug_Bulul = Bard('🎸Буг Булюль', 6, 47, 12, 12, 1, 2, 3, 0, 1, 3, 15, 1, 1)
