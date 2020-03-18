<<<<<<< HEAD
#Проект GitHub 0.Быстрый старт
#Author Daria Zaytseva
#Guess the number
=======
# Проект GitHub 0.Быстрый старт
# Author Daria Zaytseva
# Guess the number
# Программа "Угадай число!"
import numpy as np
import random
def game_core_v_by_DZ(number):
    count = 0                            # счетчик попыток
    number = np.random.randint(1,100)    # загадали число
    begin = 0                              # нижняя граница
    end = 100                              # верхняя граница
    predict = 0
    while number!=predict:               # пока загаданное число не равно нашему предполагаемому числу
            count+=1                     # увеличиваем счетчик
            predict = (end+begin)//2     # делим пополам, находя медиану, округляя до целого
            if number>predict:           # сужаем границы в зависимости от того больше или меньше загаданного числа наше предполагаемое число
             begin=predict
            elif number<predict:
             end=predict
    return(count)

# Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
def score_game(game_core_v_by_DZ,size=1000):#по умолчанию 1000 элементов - необязательный параметр
    count_ls = []                         # создаем пустой список для заполнения попытками угадывания
    np.random.seed(1)                     # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим
    random_array = np.random.randint(1, 101, size) #заполняем массив из 2000 элементов случайными числами
    for number in random_array:           #начинаем перебор загаданных компьютером чисел
        count_ls.append(game_core_v_by_DZ(number))        #заполняем список числом попыток при угадывании каждого числа из массива random_array                                                    
    score = int(np.mean(count_ls))      #вычисляем среднее арифметическое массива, заполненного количествами попыток count_ls
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток") #печатаем число попыток
    return(score)                       #возвращаем число попыток

# запускаем
size=2000 #можем менять тут число элементов в массиве
score_game(game_core_v_by_DZ) 
>>>>>>> test2
