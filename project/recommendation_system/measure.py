import math
import numpy as np
import matplotlib.pyplot as plt

#ДРЕВЕСНАЯ МЕРА БЛИЗОСТИ - для классификации
def tree_distance(dog1, dog2):
    distance = 0
    for key in dog1:
        if key in ['№ группы']:
            if dog1[key] != dog2[key]:
                return 0
            else:
                distance += 1
        if key in ['№ секции']:
            if dog1[key] != dog2[key]:
                return distance / 2
            else:
                distance += 1
    return distance / 2

def tree_distance_length(dog1, dog2):
    for key in dog1:
        if key in ['№ группы']:
            if dog1[key] != dog2[key]:
                return 4
        if key in ['№ секции']:
            if dog1[key] != dog2[key]:
                return 2
    return 0

#КОЭФФИЦИЕНТ ЖАККАРА как ассоциативная мера близости (пересечение на объединение) - для страны происхождения
def coefficient_jacquard_country(dog1, dog2):
    for key in dog1:
        if key in ['страна происхождения']:
            intersection = dog1[key].intersection(dog2[key])
            union = dog1[key].union(dog2[key])
    return len(intersection) / len(union)

#КОЭФФИЦИЕНТ ЖАККАРА как ассоциативная мера близости (пересечение на объединение) - для специализации
def coefficient_jacquard_specialization(dog1, dog2):
    for key in dog1:
        if key in ['специализация']:
            intersection = dog1[key].intersection(dog2[key])
            union = dog1[key].union(dog2[key])
    return len(intersection) / len(union)

#КОСИНУСНОЕ РАССТОЯНИЕ - для среднего роста, среднего веса, средней продолжительности жизни
def cos_distance(dog1, dog2):
    dot_product = 0
    for key in dog1:
        if key in ['средний рост', 'средний вес', 'средняя продолжительность жизни']:
            dot_product += abs(dog1[key] - dog2[key])
    
    c1 = 0
    for key in dog1:
        if key in ['средний рост', 'средний вес', 'средняя продолжительность жизни']:
            c1 += dog1[key] ** 2
    magnitude_dog1 = math.sqrt(c1)
    
    c2 = 0
    for key in dog2:
        if key in ['средний рост', 'средний вес', 'средняя продолжительность жизни']:
            c2 += dog2[key] ** 2
    magnitude_dog2 = math.sqrt(c2)

    distance = 1 - (dot_product / (magnitude_dog1 * magnitude_dog2))
    return distance

#КОЭФФИЦИЕНТ ЖАККАРА как ассоциативная мера близости (пересечение на объединение) - для шерсти
def coefficient_jacquard_wool(dog1, dog2):
    for key in dog1:
        if key in ['длина шерсти']:
            intersection1 = dog1[key].intersection(dog2[key])
            union1 = dog1[key].union(dog2[key])

    for key in dog1:
        if key in ['тип волоса']:
            intersection2 = dog1[key].intersection(dog2[key])
            union2 = dog1[key].union(dog2[key])

    for key in dog1:
        if key in ['структура']:
            intersection3 = dog1[key].intersection(dog2[key])
            union3 = dog1[key].union(dog2[key])

    for key in dog1:
        if key in ['подшёрсток']:
            intersection4 = dog1[key].intersection(dog2[key])
            union4 = dog1[key].union(dog2[key])
    
    len_intersection = len(intersection1) + len(intersection2) + len(intersection3) + len(intersection4)
    len_union = len(union1) + len(union2) + len(union3) + len(union4)
    
    return len_intersection / len_union

#АССОЦИАТИВНАЯ МЕРА БЛИЗОСТИ (количество совпадений на общее количество) - для обучаемости и активности
def associative(dog1, dog2):
    distance = 0
    k = 0
    for key in dog1:
        if key in ['активность', 'обучаемость']:
            if (dog1[key] == dog2[key]):
                distance += 1
            k += 1
    # distance - количество совпадений; k - всего характеристик
    return distance / k

#КОЭФФИЦИЕНТ ЖАККАРА как ассоциативная мера близости (пересечение на объединение) - для условий содержания
def coefficient_jacquard_life(dog1, dog2):
    for key in dog1:
        if key in ['помещение']:
            intersection1 = dog1[key].intersection(dog2[key])
            union1 = dog1[key].union(dog2[key])

    for key in dog1:
        if key in ['доп факты']:
            intersection2 = dog1[key].intersection(dog2[key])
            union2 = dog1[key].union(dog2[key])
    
    len_intersection = len(intersection1) + len(intersection2)
    len_union = len(union1) + len(union2)
    
    return len_intersection / len_union

#МАНХЭТТЕНСКОЕ РАССТОЯНИЕ - для бинарных значений
def manhattan_distance_bin(dog1, dog2):
    distance = 0
    for key in dog1:
        if key in ['нужен ли опыт владельцу?', 'подходит ли для семьи с детьми?']:
            distance += abs(dog1[key] - dog2[key])
    if distance == 0:
        return 1
    elif distance == 1:
        return 0.5
    else:
        return 0

#МОЯ МЕРА БЛИЗОСТИ
def myMeasure(dog1, dog2):
    value1 = tree_distance(dog1, dog2)
    #print(value1)
    value2 = coefficient_jacquard_country(dog1, dog2)
    #print(value2)
    value3 = coefficient_jacquard_specialization(dog1, dog2)
    #print(value3)
    value4 = cos_distance(dog1, dog2)
    #print(value4)
    value5 = coefficient_jacquard_wool(dog1, dog2)
    #print(value5)
    value6 = associative(dog1, dog2)
    #print(value6)
    value7 = coefficient_jacquard_life(dog1, dog2)
    #print(value7)
    value8 = manhattan_distance_bin(dog1, dog2)
    #print(value8)
    return (value1 + value2 + value3 + value4 + value5 + value6 + value7 + value8)/8
