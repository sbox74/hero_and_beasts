#!/usr/bin/env python3

import random

# рыцарь
knight_health = 10
knight_strength = 10
# чудовище
beast_health = None
beast_strength = None
# яблоко здоровья
apple = None
# меч (сила)
sword = None
# этап игры
stage = 1
# текущее количество побед
wins = 0
# необходимое количество побед
wins_count = 10
# объекты в игре
object_list = ('beast','sword', 'apple')

# генератор здоровья/силы
def strength_health_gen() -> int:
    value = random.randint(5,15)
    return value

# генератор текущего объекта игры
def change_object(obj: tuple) -> str:
    return random.choice(obj)

# обработка ввода клавиш
def key_handler() -> str:
    while True:
        user_key = input()
        if user_key not in ['1', '2']:
            print('Введено неверное значение. Введите 1 или 2:')
            continue
        else:
            break
    return user_key
    

print('Герой и чудовища')
print('')


# главный цикл
while wins < wins_count:
    print('Шаг: ', stage)
    next_object = change_object(object_list)
    print(f'Рыцарь. Сила атаки: {knight_strength}, Здоровье: {knight_health}')

    if next_object == 'apple':
        apple = strength_health_gen()
        print('Найдено яблоко здоровья')
        print('Нажмите: 1 или 2 - съесть')
    if next_object == 'sword':
        sword = strength_health_gen()
        print(f'Найден меч. Сила атаки: {sword}')
        print('Нажмите: 1 - взять, 2 - пройти мимо')
    if next_object == 'beast':
        beast_health = strength_health_gen()
        beast_strength = strength_health_gen()
        print(f'Впереди чудовище. Сила атаки: {beast_strength} Здоровье: {beast_health}')
        print('Нажмите: 1 - атаковать, 2 - убежать')

    user_key = key_handler()
    
    if user_key == '1':
        if next_object == 'apple':
            knight_health += apple
            print(f'Прибавка к здоровью: {apple}')
        if next_object == 'sword':
            knight_strength = sword
        if next_object == 'beast':
            knight_health -= beast_strength
            beast_health -= knight_strength
            if knight_health <= 0:
                break
            if beast_health <= 0:
                wins += 1
                #print(f'Чудовищ убито: {wins}')
                

    if user_key == '2':
        if next_object == 'apple':
            knight_health += apple
            print(f'Прибавка к здоровью: {apple}')
             
    stage += 1
    print('')

         
if wins == wins_count:
    print('Победа!')
else:
    print('Игра окончена')



