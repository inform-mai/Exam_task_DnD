from main import *


class Boss(Human):
    def __init__(self, name, level, hp, ac, mp, strenght, agility, physique, iq, wisdom, charisma, saveroll,
                 action, baction):
        super().__init__(name, level, hp, ac, mp, strenght, agility, physique, iq, wisdom, charisma, action, baction)
        self.saveroll = saveroll
        self.weapons = ['Ритуальный нож клана Судума', 'Коса Бога смерти']
        self.artifacts = ['Кольцо призыва Элементаля', 'Кольцо Разума']
        self.skills = ['Исцеление Мелодией', 'Суд Ума']
        self.spells = ['Огненный Шар', 'Пляшущая Молния', 'Силовая Волна', 'Стена Ветров']
        self.mx_mp = self.mp
        self.start_action = self.action
        self.start_baction = self.baction

    def choice_weapon_or_spell(self) -> int:
        if randint(1, 2) == 1:
            wos = 1
            return wos
        else:
            wos = 2
            return wos

    def choice_weapon(self, wos) -> int:
        if wos == 1:
            if self.action > 0:
                total_weapon = randint(0, 1)
                return total_weapon
            else:
                pass
        else:
            pass

    def choice_spell(self, wos) -> int:
        if wos == 2:
            if self.action > 0:
                total_spell = randint(0, 3)
                return total_spell
            else:
                pass
        else:
            pass

    def choice_artifact(self) -> int:
        if self.hp <= self.mx_hp // 2:
            print(
                f'{self.name} готов использовать свои последние козыри ради победы, даже если это навредит ему самому...')
            possible_use = randint(1, 4)
            if possible_use == 4:
                total_artifact = randint(0, 1)
                return total_artifact
            else:
                pass
        else:
            pass

    def choice_skill(self) -> int:
        if self.baction > 0:
            total_skill = randint(0, 1)
            return total_skill
        else:
            pass

    def attack(self, wos:int, target:"Human", total_weapon:int, total_spell:int):
        if self.action > 0:
            if wos == 1:
                if total_weapon == 0:
                    if self.hit(target, 0):
                        damage = self.roll_d4() + self.strenght - 1
                        target.hp -= damage
                        target.ac -= 1
                        print(
                            f'{self.name} Нанёс {target.name} {damage} урона с помощью {self.weapons[total_weapon]} и изуродовал броню {target.name}: КД = {target.ac}...')
                    self.action -= 1
                elif total_weapon == 1:
                    if self.hit(target, 0):
                        damage_heal = self.roll_d6() + self.roll_d6() - 1
                        target.hp -= damage_heal
                        self.hp += damage_heal
                        print(
                            f'{self.name} Нанёс {target.name} {damage_heal} урона с помощью {self.weapons[total_weapon]} и исцелил себя чужой кровью...')
                    self.action -= 1
            elif wos == 2 and self.mp > 0:
                if total_spell == 0 and self.mp >= 2:
                    if target.make_saveroll() < self.saveroll:
                        damage = self.roll_d6() + self.roll_d6() + self.roll_d6() + self.iq
                        target.hp -= damage
                        print(f'{self.name} Нанёс {target.name} {damage} урона с помощью {self.spells[total_spell]}...')
                    self.action -= 1
                    self.mp -= 2
                elif total_spell == 1 and self.mp >= 2:
                    if self.hit(target, 0):
                        damage = self.roll_d10() + self.roll_d6() + self.iq
                        target.hp -= damage
                        print(f'{self.name} Нанёс {target.name} {damage} урона с помощью {self.spells[total_spell]}...')
                    else:
                        damage = (self.roll_d10() + self.roll_d6() + self.iq) // 2
                        target.hp -= damage
                        print(f'{self.name} Нанёс {target.name} {damage} урона с помощью {self.spells[total_spell]}...')
                    self.action -= 1
                    self.mp -= 2
                elif total_spell == 2 and self.mp >= 4:
                    if target.make_saveroll() < self.saveroll:
                        damage = self.roll_d10() + self.roll_d10() + self.iq
                        target.hp -= damage
                        print(f'{self.name} Нанёс {target.name} {damage} урона с помощью {self.spells[total_spell]}...')
                    self.action -= 1
                    self.mp -= 4
                elif total_spell == 3:
                    cnt_persons = 2
                    while cnt_persons > 0 and self.mp >= 6:
                        if target.make_saveroll() < self.saveroll:
                            damage = self.roll_d8() + self.roll_d8() + self.roll_d8() + self.roll_d4() + self.iq
                            target.hp -= damage
                            print(
                                f'{self.name} Нанёс {target.name} {damage} урона с помощью {self.spells[total_spell]}...')
                        cnt_persons -= 1
                    self.action -= 1
                    self.mp -= 6
        else:
            pass

    def use_skill(self, total_skill:int, target:"Human"):
        if self.baction > 0:
            if total_skill == 0:
                self.hp += self.roll_d10() + self.iq
                self.hp = self.is_mx_hp()
                self.baction -= 1
                print(f'{self.name} использовал умение: {self.skills[total_skill]}, и немного стал здоровее!')
            elif total_skill == 1:
                if target.make_saveroll() < self.saveroll:
                    mx_stat = max(target.strenght, target.agility, target.physique, target.iq, target.wisdom,
                                  target.charisma)
                    mx_stat -= 1
                    print(
                        f'{self.name} использовал умение: {self.skills[total_skill]}, и обратил сильные стороны {target.name} в прах!')
                self.baction -= 1
        else:
            pass

    def use_artifact(self, total_artifact:int, target:"Human"):
        if total_artifact == 0:
            self.hp -= self.roll_d12()
            cnt_elementals = 2
            while cnt_elementals > 0:
                elemental = randint(1, 4)
                if elemental == 1:
                    print('Призван Огненный Элементаль!..')
                    if self.hit(target, 0):
                        damage = self.roll_d8() + self.roll_d8()
                        target.hp -= damage
                        print(f'Жгучее прикосновение! Огненный Элементаль нанёс {target.name} {damage} урона!')
                    elif target.make_saveroll() < self.saveroll:
                        target.action -= 1
                        print(
                            f'{target.name} ослаб после взгляда Огненного Элементаля! -1 действие: {target.action}/{target.mx_action}')
                if elemental == 2:
                    print('Призван Водяной Элементаль!..')
                    if self.hit(target, 0):
                        damage = self.roll_d8() + self.roll_d8()
                        target.hp -= damage
                        print(f'Хлыст волной! Водяной Элементаль нанёс {target.name} {damage} урона!')
                    elif target.make_saveroll() < self.saveroll:
                        target.action -= 1
                        print(
                            f'{target.name} ослаб после взгляда Водяного Элементаля! -1 действие: {target.action}/{target.mx_action}')
                if elemental == 3:
                    print('Призван Земляной Элементаль!..')
                    if self.hit(target, 0):
                        damage = self.roll_d8() + self.roll_d8()
                        target.hp -= damage
                        print(f'Размашистый! Земляной Элементаль нанёс {target.name} {damage} урона!')
                    elif target.make_saveroll() < self.saveroll:
                        target.action -= 1
                        print(
                            f'{target.name} ослаб после взгляда Земляного Элементаля! -1 действие: {target.action}/{target.mx_action}')
                if elemental == 4:
                    print('Призван Воздушный Элементаль!..')
                    if self.hit(target, 0):
                        damage = self.roll_d8() + self.roll_d8()
                        target.hp -= damage
                        print(f'Вихрь! Воздушный Элементаль нанёс {target.name} {damage} урона!')
                    elif target.make_saveroll() < self.saveroll:
                        target.action -= 1
                        print(
                            f'{target.name} ослаб после взгляда Воздушного Элементаля! -1 действие: {target.action}/{target.mx_action}')
                cnt_elementals -= 1
        elif total_artifact == 1:
            self.hp -= self.roll_d12()
            act_or_bact = randint(1, 2)
            if act_or_bact == 1:
                self.action += 1
            else:
                self.baction += 1
            print(
                f'{self.name} использовал {self.artifacts[total_artifact]} и стал вдумчивее и быстрее продумывать свои атаки...')

    def block_turn(self, enemy:list["Human"]):
        if self.is_alive():
            while self.action > 0 or self.baction > 0:
                choice_wos = self.choice_weapon_or_spell()
                choice_weapon = self.choice_weapon(choice_wos)
                choice_spell = self.choice_spell(choice_wos)
                choice_artifact = self.choice_artifact()
                choice_skill = self.choice_skill()
                choiced_hero = enemy[randint(0, 3)]
                while choiced_hero.hp <= 0:
                    choiced_hero = enemy[randint(0, 3)]
                self.attack(choice_wos, choiced_hero, choice_weapon, choice_spell)
                self.use_skill(choice_skill, choiced_hero)
                self.use_artifact(choice_artifact, choiced_hero)
            self.action = self.start_action
            self.baction = self.start_baction


Sirex = Boss('♆Сайрекс', 12, 200, 15, 14, 3, 2, 2, 5, 2, 3, 15, 2, 1)
