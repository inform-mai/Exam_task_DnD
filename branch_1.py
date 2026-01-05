from Utils import *
from ksandr_player import *
from garou import *
from log_in_account import *

artifact_1 = {}
flag_death_player = 0
persons = [Ksandr, Garou]
tracker_list = tracker_initiative(persons)
mercy_garou = 0
while (Ksandr.hp>0 and Garou.hp>0) and mercy_garou!=1:
     for person in tracker_list:
         print(f'{'-'*25}\nХод {person[0].name}!\n{'-'*25}')
         if person[0] == Ksandr:
             person[0].block_turn(Garou)
             flag_mercy = person[0].analysising(15)
             if person[0].analysising_garou(flag_mercy):
                 mercy_garou = 1
         elif person[0] == Garou and mercy_garou!=1:
             person[0].block_turn(Ksandr)

if mercy_garou == 0:
    if Ksandr.hp <= 0:
        flag_death_player = 1
        print('===Игра окончена===\n К сожалению, ты погиб, и тебе не удалось спасти мир!...')
    if Garou.hp <= 0:

        print(
            f'Поздравляю! Ты одержал победу над {Garou.name}, но теперь, переступая через труп бывшего товарища, надо идти дальше...')
else:
    if Garou.hp > 0:
        Garou.hp = Garou.mx_hp
        Garou.mp = Garou.mx_mp
        print(
            f'{Garou.name}: Спасибо тебе ещё раз! Знаешь, я себе прикарманил 1 забавную вещицу, артефакт что-ли какой-то...'
            'В общем, дарю!')
        artifact_1[
            'Браслет \Последний Удар/'] = 'Когда твоё ХП опускается до значения, меньшего четверти от максимального здоровья, твоя сила увеличивается вдвое!'
        print(f'АРТЕФАКТ НАЙДЕН! Браслет \Последний Удар/ - Когда твоё ХП опускается до значения, меньшего четверти от максимального здоровья, твоя сила увеличивается вдвое!')
    else:
        print(f'{Ksandr.name}: **Твою же ж матушку... ЧТО ЖЕ Я РАНЬШЕ НЕ ДОДУМАЛСЯ СКАЗАТЬ ЭТОГО!!!!????**')
        print('.......')
        print(f'{Ksandr.name}: Башка тупая!')
        print(f'{Ksandr.name}: Ладно, надо идти дальше. Хотя стоп, у него что-то вывалилось из кармана...')
        Ksandr.artifacts[
            'Браслет \Последний Удар/'] = 'Когда твоё ХП опускается до значения, меньшего четверти от максимального здоровья, твоя сила увеличивается вдвое!'
        print(f'АРТЕФАКТ НАЙДЕН! {list(Ksandr.artifacts.keys())[0]} - {Ksandr.artifacts['Браслет \Последний Удар/']}')

print('Что ж, далее следует направиться в Заброшенную шахту. Там запрятана мерзким Сайрексом Вуль Гуль!')
Ksandr.hp=Ksandr.mx_hp

import branch_2