from branch_3 import *

if not flag_death_player:
    persons = [Ksandr,Sirex]
    if mercy_garou:
        persons.append(Garou)
    if vul_gul_save:
        persons.append(Vul_Gul)
    if save_bug_bulul:
        persons.append(Bug_Bulul)


    print('''Добравшись до Эпицентра Элименталии, ты видишь, как на троне из костей прямо перед пропастью восседает он...
    ♆Сайрекс...
    Он с большой улыбкой смотрит на тебя...
    
    🛡Ксандр Вин: Ну вот мы и встретились, Сайрекс!
    ♆Сайрекс: Даа, Ксандр Вин, не ожидал, что ты доберёшься настолько далеко и я смогу увидеть тебя в последний раз!
    🛡Ксандр Вин: Это ты верно подметил, в последний раз... Ведь больше ты не увидишь свет после меня.
    ♆Сайрекс: В таком случае, сразимся и поймём, что действительно правит миром: добро или зло?..''')

    flag_win = 0
    tracker_list = tracker_initiative(persons)

    while all(person[0].hp>0 for person in tracker_list if person[0]!=Sirex) and Sirex.hp>0:
        for person in tracker_list:
            print(f'{'-' * 25}\nХод {person[0].name}!\n{'-' * 25}')
            if person[0] == Ksandr:
                person[0].block_turn(Sirex)
            elif person[0] == Vul_Gul:
                person[0].block_turn(Sirex)
            elif person[0] == Bug_Bulul:
                person[0].block_turn(Sirex)
            elif person[0] == Garou:
                person[0].block_turn(Sirex)
            elif person[0] == Sirex:
                person[0].block_turn(persons)

    if Sirex.hp<=0:
        flag_win = 1

    if flag_win:
        print('Ура победа!')
    else:
        print('===Игра окончена===\n К сожалению, ты погиб, и тебе не удалось спасти мир!...')
else:
    pass