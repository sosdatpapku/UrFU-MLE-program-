import numpy as np
from numpy import random

def rand_numb(number) -> int:
    """Компьютер угадывает случайное число
    Args:
        number (int, optional): Загаданное число.
    Returns:
        int: Число попыток
    """
    predict_numb = np.random.randint(1, 101) # загадываем случайное число, используя генератор случайных чисел
    count = 0 # Переменная счетчик
    min_numb = 1 # Минимальное значение загадываемого числа
    max_numb = 100 # Максимальное значение загадываемого числа
    while True:
        count += 1
        if predict_numb > number: 
            max_numb = predict_numb - 1 # сдвигаем верхнюю границу
            predict_numb = (max_numb + min_numb) // 2
        elif predict_numb < number:
            min_numb = predict_numb + 1 # сдвигаем нижнюю границу
            predict_numb = (max_numb + min_numb) // 2
        else:
            break # число отгадано - выход из цикла
    return(count)

def score_game(rand_numb) -> int:
    """ За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_list = [] # здесь будем хранить значения затраченных попыток за один проход алгоритма
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_list = np.random.randint(1, 101, size=(1000))  # загадали список из 1000 случайных чисел
    for number in random_list: 
        count_list.append(rand_numb(number)) # добавляем значение количества затраченных попыток
    score = int(np.mean(count_list)) # вычисляем среднее значение затраченных попыток
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

score_game(rand_numb) # RUN
