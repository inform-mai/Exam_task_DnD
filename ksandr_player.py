from main import *
from garou import *
from bug_bulul import *
from vul_gul import *
from sirex_boss import *
from time import *

class Warrior(Human):
    def __init__(self, name, level, hp, ac, mp, strenght, agility, physique, iq, wisdom, charisma, action, baction):
        super().__init__(name, level, hp, ac, mp, strenght, agility, physique, iq, wisdom, charisma, action, baction)
        self.weapons = {'Секира': 'урон - 1d12', 'Коваль Небес': 'урон - 1d6+1d8'}
        self.keys_weapons = list(self.weapons.keys())
        self.skills = {'Второе дыхание': '+1d8 к здоровью', 'Всплеск действий': '+1 действие!'}
        self.keys_skills = list(self.skills.keys())
        self.TBS = 3
        self.mx_TBS = self.TBS
        self.techniques = {'Точный удар': '+1d8 к попаданию', 'Атака с финтом': '+1d8 к урону'}
        self.keys_techniques = list(self.techniques.keys())
        self.start_action = self.action
        self.start_baction = self.baction
        self.analysis = 1
        self.mx_analysis = self.analysis

    def analysising(self, difficulty:int) -> int:
        if self.analysis > 0 and randint(1,4)==4:
            print(
                'Ты можешь проанализировать ситуацию и хорошенько подумать. У тебя 1 попытка! Тебе нужно выбросить больше установленной сложности броска!\nВведи 1, если хочешь подумать или 0, если хочешь продолжить бой:',
                end=' ')
            while True:
                try:
                    roll_flag = int(input())
                    if roll_flag == 0 or roll_flag == 1:
                        break
                except ValueError:
                    print('Некорректный ввод числа!')
            if roll_flag:
                total_analysis = 0
                roll_analysis = self.roll_d20() + self.iq
                print(f'1d20+iq: {roll_analysis}')
                if roll_analysis >= difficulty:
                    total_analysis = 1
                    print('Отлично! Ты что-то понял...')
                else:
                    print('Увы, Не удалось ничего понять!')
                self.analysis -= 1
                return total_analysis
            else:
                pass
        else:
            pass

    def analysising_garou(self, total_analysis:int) -> int:
        if total_analysis:
            print('''Ты понимаешь, что Сайрекс каким-то образом надавил на Гароу, чтобы тот примкнул к нему!
            Ответ лежит на поверхности...
            Похоже, Сайрекс намекнул о том, что контракт, который Гароу заключил с дьяволом, может распасться, если Колдун не поможет гадкому злодею.
            Однако ты вспоминаешь, что никто, кроме Гароу либо его дьявола-покровителя, не может вмешаться в их сделку.
            **Видимо, Сайрекс как-то запугал колдуна и надавил на его слабое место**
            Возможно, стоит уговорить Гароу и объяснить ему, в чём дело...\n''')
            print(
                'Ты можешь пощадить Гароу и уговорить его от этого бессмысленного боя. Введи 1, если хочешь уговорить, и 0, если хочешь продолжить бой:\n')
            while True:
                try:
                    flag_mercy_garou = int(input())
                    if flag_mercy_garou in [0, 1]:
                        break
                except ValueError:
                    print('Некорректный ввод числа!')
            if flag_mercy_garou:
                print('''🛡Ксандр Вин: Послушай, Гароу! Неужели ты забыл, что твой контракт с дьяволом не может измениться или вовсе уничтожиться из-за такого урода, как Сайрекс?
                Давай забудем наши ссоры и вместе победим этого гадкого злодея!!!''')
                print('''🪄Гароу: Мир!.. Уж прости меня, я совсем забылся о том, как работает то, что мне даёт это могущество и силу...
                Спасибо тебе! Я обязательно тебе помогу...''')
                return flag_mercy_garou
            else:
                print('Бой продолжается...')
                pass
        else:
            pass

    def analysising_bug_bulul(self,total_analysis:int,vul_gul_save:int) -> int:
        if total_analysis:
            print('''Ты понимаешь, что Сайрекс каким-то образом запудрил голову Буг Булюль, чтобы та примкнула к нему!
            Ответ лежит на поверхности...
            Ты видишь в глазах дварфийки полную пустоту
            По всей видимости, её загипнотизировал этот грёбаный Сайрекс
            Возможно, что-то действительно дорогое для Буг Булюль сможет ей проснуться из рабского сна...''')
            print(
                'Ты можешь спасти Буг Булюль и привести её в чувства! Введи 1, если хочешь спасти, и 0, если не хочешь:')
            while True:
                try:
                    flag_save_bug_bulul = int(input())
                    if flag_save_bug_bulul in [0,1]:
                        break
                except ValueError:
                    print('Некорректный ввод числа!')
            if flag_save_bug_bulul and vul_gul_save:
                print('''🛡Ксандр Вин: Послушай, Буг Булюль! Очнись же! Вот, смотри, здесь твоя любимая дочь!
                🛡Ксандр Вин: Не дай же этому мерзавцу отобрать у тебя самое дорогое, что есть в твоей жизни!
                🛡Ксандр Вин: ОЧНИСЬ!!!''')
                sleep(10)
                print('🛡Ксандр Вин: .....')
                sleep(5)
                print('''🎸Буг Булюль: ВАААЙЙЯЯ, ВУУУЛЬ ГУУУЛЬ!!!!
                🗡️Вуль гуль: МАМММААААААА ЁКАЛАМЕНЕ!!!!
                🛡Ксандр Вин: *Да, всегда приятно на душе видеть, когда семья воссоединяется)*
                🛡Ксандр Вин: Так, девушки, это всё конечно прекрасно, однако нам пора двигаться дальше!
                🎸Буг Булюль: Вайя, Ксандрик, дорогой!! Спасибо тебе большое за то, что спас меня!!''')
                return flag_save_bug_bulul
            elif flag_save_bug_bulul and not vul_gul_save:
                print('''🛡Ксандр Вин: Послушай, Буг Булюль! Очнись же! Вот, смотри, здесь твоя любимая дочь!
                🛡Ксандр Вин: Не дай же этому мерзавцу отобрать у тебя самое дорогое, что есть в твоей жизни!
                🛡Ксандр Вин: ОЧНИСЬ!!!''')
                sleep(10)
                print('🛡Ксандр Вин: .....')
                sleep(5)
                print('''🛡Ксандр Вин: Видимо, одними словами тут не поможешь...
                Бой продолжается!''')
            elif not flag_save_bug_bulul:
                print('Бой продолжается!')
                pass
        else:
            pass


    def choice_weapon(self) -> str:
        if self.action > 0:
            print(
                f'У тебя осталось {self.action}/{self.mx_action} действий, можешь потратить 1 на атаку\nВыбери оружие, написав его номер:')
            for i in range(len(self.weapons)):
                print(f'{i + 1}) {self.keys_weapons[i]} - {self.weapons[self.keys_weapons[i]]} ')
            while True:
                try:
                    choice_flag = int(input())
                    if choice_flag == 1 or choice_flag == 2:
                        break
                except ValueError:
                    print('Некорректный ввод числа!')
            total_choice = choice_flag - 1
            print(f'Выбрано: {self.keys_weapons[total_choice]}')
            return self.keys_weapons[total_choice]
        else:
            pass

    def choice_technique(self) -> str:
        if self.TBS > 0:
            print(
                f'Ты можешь при атаке использовать Приём, но лишь 3 раза за всё время: {self.TBS}/{self.mx_TBS}\nВведи 1, если хочешь и 0, если не хочешь:')
            while True:
                try:
                    technique_use_flag = int(input())
                    if technique_use_flag == 0 or technique_use_flag == 1:
                        break
                except ValueError:
                    print('Некорректный ввод числа!')
            if technique_use_flag:
                print(f'Введи номер приёма, который хочешь выбрать:')
                for i in range(len(self.techniques)):
                    print(f'{i + 1}) {self.keys_techniques[i]} - {self.techniques[self.keys_techniques[i]]}')
                while True:
                    try:
                        technique_flag = int(input())
                        if technique_flag in [1, 2]:
                            break
                    except ValueError:
                        print('Неккоректный ввод числа!')
                total_technique = self.keys_techniques[technique_flag - 1]
                print('Выбран приём:', total_technique)
                self.TBS -= 1
                return total_technique
            else:
                pass
        else:
            pass

    def choice_skill(self) -> str:
        if self.baction > 0:
            print(
                f'Ты можешь использовать 1 умение, это будет стоить 1 бонусное действие: {self.baction}/{self.mx_baction}')
            print('Введи номер умения, которое хочешь выбрать:')
            for i in range(len(self.skills)):
                print(f'{i + 1}) {self.keys_skills[i]} - {self.skills[self.keys_skills[i]]}')
            while True:
                try:
                    baction_flag = int(input())
                    if baction_flag in [1, 2]:
                        break
                except ValueError:
                    print('Некорректный ввод числа!')
            total_skill = self.keys_skills[baction_flag - 1]
            print('Выбрано умение:', total_skill)
            return total_skill
        else:
            pass

    def use_skill(self, total_skill):
        if self.baction > 0:
            if total_skill == 'Второе дыхание':
                heal = self.roll_d8()
                self.hp += heal
                self.is_mx_hp()
                self.baction -= 1
                print(f'{self.name} Восстановил {heal} ХП!')
            elif total_skill == 'Всплеск действий':
                self.action += 1
                self.baction -= 1
                print(f'У {self.name} добавилось 1 действие!')
        else:
            pass

    def attack(self, weapon, target, technique):
        if self.action > 0:
            hit = self.hit(target, technique) > 0
            if weapon == 'Секира':
                if hit:
                    self.action -= 1
                    damage = self.roll_d12() + self.strenght
                    if technique == 'Атака с финтом':
                        damage += self.roll_d8()
                    target.hp -= damage
                    print(f'{target.name} Нанесено {damage} урона!')
                else:
                    self.action -= 1
                    pass
            elif weapon == 'Коваль Небес':
                if hit:
                    self.action -= 1
                    damage = self.roll_d6() + self.roll_d8() + self.strenght
                    if technique == 'Атака с финтом':
                        damage += self.roll_d8()
                    target.hp -= damage
                    print(f'{target.name} Нанесено {damage} урона!')
                else:
                    self.action -= 1
                    pass
            else:
                pass
        else:
            pass

    def block_turn(self, enemy:"Human"):
        if self.is_alive():
            while self.action > 0 or self.baction > 0:
                choice_weapon_1 = self.choice_weapon()
                choice_skill_1 = self.choice_skill()
                choice_technique_1 = self.choice_technique()
                self.use_skill(choice_skill_1)
                self.attack(choice_weapon_1, enemy, choice_technique_1)
            self.action = self.start_action
            self.baction = self.start_baction


Ksandr = Warrior('🛡Ксандр Вин', 6, 60, 17, 0, 3, 2, 2, 1, 0, 1, 2, 1)
