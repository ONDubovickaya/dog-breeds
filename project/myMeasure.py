import math
import numpy as np
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

def color_matrix(matrix):
    colors = {}  # Словарь для хранения цветов
    color_matrix = []  # Итоговая раскрашенная матрица
    vmax = np.max(matrix)

    for row in matrix:
        colored_row = []  # Раскрашенная строка матрицы
        for value in row:
            if value in colors:  # Если значение встречается ранее
                colored_row.append(colors[value])
            else:  # Если значение встречается впервые
                color = plt.cm.RdYlBu_r(value/vmax)  # Вычисляем цвет в зависимости от значения
                colored_row.append(color)
        color_matrix.append(colored_row)
    
    return color_matrix

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
  
# Массив словарей с объектами
data = [
    {'id': 1, 'название': 'Сибирский хаски', '№ группы': 5, '№ секции': 1, 'название секции': 'Северные ездовые собаки', 'страна происхождения': {'Россия'}, 'специализация': {'ездовая собака'}, 'средний рост': 55.5, 'средний вес': 21.5, 'средняя продолжительность жизни': 12, 'обучаемость': 'умеренная', 'активность': 'высокая', 'длина шерсти': {'средняя'}, 'тип волоса': {'двойной'}, 'структура': {'плотная'}, 'подшёрсток': {'плотный'}, 'помещение': {'просторное', 'загородное'}, 'доп факты': {'просторный двор'}, 'нужен ли опыт владельцу?': 1, 'подходит ли для семьи с детьми?': 1},
    {'id': 2, 'название': 'Самоедская лайка', '№ группы': 5, '№ секции': 1, 'название секции': 'Северные ездовые собаки', 'страна происхождения': {'Россия'}, 'специализация': {'ездовая собака', 'охотничья собака (на мелкую дичь)'}, 'средний рост': 51, 'средний вес': 26.5, 'средняя продолжительность жизни': 12, 'обучаемость': 'средняя', 'активность': 'выше среднего', 'длина шерсти': {'длинная'}, 'тип волоса': {'двойной'}, 'структура': {'плотная'}, 'подшёрсток': {'плотный'}, 'помещение': {'просторное'}, 'доп факты': {'доступ к прогулкам на природе'}, 'нужен ли опыт владельцу?': 0, 'подходит ли для семьи с детьми?': 1},
    {'id': 3, 'название': 'Ротвейлер', '№ группы': 2, '№ секции': 2, 'название секции': 'Молоссы', 'страна происхождения': {'Германия'}, 'специализация': {'служебная собака', 'сторожевая собака', 'собака-поводырь'}, 'средний рост': 63.5, 'средний вес': 45.5, 'средняя продолжительность жизни': 11.5, 'обучаемость': 'высокая', 'активность': 'выше среднего', 'длина шерсти': {'короткая'}, 'тип волоса': {'прямой', 'грубый'}, 'структура': {'густая'}, 'подшёрсток': {'плотный'}, 'помещение': {'с укреплённым забором', 'загородное'}, 'доп факты': {'просторный двор'}, 'нужен ли опыт владельцу?': 1, 'подходит ли для семьи с детьми?': 0},
    {'id': 4, 'название': 'Немецкая овчарка', '№ группы': 1, '№ секции': 1, 'название секции': 'Пастушьи собаки', 'страна происхождения': {'Германия'}, 'специализация': {'служебная собака'}, 'средний рост': 60.5, 'средний вес': 38.5, 'средняя продолжительность жизни': 12.5, 'обучаемость': 'высокая', 'активность': 'высокая', 'длина шерсти': {'средняя'}, 'тип волоса': {'прямой'}, 'структура': {'густая'}, 'подшёрсток': {'плотный'}, 'помещение': {'просторное'}, 'доп факты': {'просторный двор'}, 'нужен ли опыт владельцу?': 1, 'подходит ли для семьи с детьми?': 0},
    {'id': 5, 'название': 'Лабрадор-ретривер', '№ группы': 8, '№ секции': 1, 'название секции': 'Ретриверы', 'страна происхождения': {'Великобритания'}, 'специализация': {'охотничья собака (поиск и подача дичи)', 'служебная собака', 'собака-поводырь'}, 'средний рост': 55.5, 'средний вес': 29.5, 'средняя продолжительность жизни': 12.5, 'обучаемость': 'высокая', 'активность': 'высокая', 'длина шерсти': {'короткая'}, 'тип волоса': {'прямой', 'волнистый'}, 'структура': {'плотная'}, 'подшёрсток': {'плотный'}, 'помещение': {'просторное'}, 'доп факты': {'просторный двор', 'близость к парку или пляжу'}, 'нужен ли опыт владельцу?': 0, 'подходит ли для семьи с детьми?': 1}
]

#print(myMeasure(data[0], data[0]))
# Размер матрицы смежности
n = len(data)

#МОЯ МЕРА БЛИЗОСТИ
# Создание пустой матрицы смежности
adjacency_matrix = np.zeros((n, n))

# Заполнение матрицы смежности для моей меры близости
print("МОЯ МЕРА БЛИЗОСТИ (чем больше значение, тем выше сходство):\n")
for i in range(n):
    for j in range(n):
        # Вычисление близости между объектами i и j
        similarity = myMeasure(data[i], data[j])
        # Запись значения близости в матрицу смежности
        adjacency_matrix[i][j] = similarity

# Преобразование матрицы смежности в DataFrame
breed_names = [obj['название'] for obj in data]
df = pd.DataFrame(adjacency_matrix, index=breed_names, columns=breed_names)
# Вывод таблицы
print(df, "\n")

upper_triangle_indices = np.triu_indices_from(adjacency_matrix, k=1)
i_values = upper_triangle_indices[0]
j_values = upper_triangle_indices[1]

similarity_values = adjacency_matrix[i_values, j_values]

sorted_indices = np.argsort(similarity_values)[::-1]
sorted_i_values = i_values[sorted_indices]
sorted_j_values = j_values[sorted_indices]
sorted_similarity_values = similarity_values[sorted_indices]

sorted_breed_names_i = [breed_names[i] for i in sorted_i_values]
sorted_breed_names_j = [breed_names[j] for j in sorted_j_values]

#Табулированный вывод списка пород
print("Табулированный список пород собак по убыванию их степени схожести: \n")
rows = []

for i, j, similarity in zip(sorted_breed_names_i, sorted_breed_names_j, sorted_similarity_values):
    rows.append([i, j, similarity])

table = tabulate(rows, headers=["Порода I", "Порода II", "Схожесть"])
print(table)

colored_matrix = color_matrix(adjacency_matrix)

arr = np.array(colored_matrix)
plt.imshow(arr, cmap='RdYlBu_r', interpolation='nearest')
plt.colorbar()
plt.title("Моя мера близости (чем темнее цвет, тем больше схожесть)")
plt.show()
