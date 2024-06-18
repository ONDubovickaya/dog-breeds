import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Radiobutton
import numpy as np
import pandas as pd
from tabulate import tabulate
from all import myMeasure

data = [
    {'id': 1, 
     'название': 'Сибирский хаски', 
     '№ группы': 5, 
     '№ секции': 1, 
     'название секции': 'Северные ездовые собаки', 
     'страна происхождения': {'Россия'}, 
     'специализация': {'ездовая собака'}, 
     'средний рост': 55.5, 
     'средний вес': 21.5, 
     'средняя продолжительность жизни': 12, 
     'обучаемость': 'умеренная', 
     'активность': 'высокая', 
     'длина шерсти': {'средняя'}, 
     'тип волоса': {'двойной'}, 
     'структура': {'плотная'}, 
     'подшёрсток': {'плотный'}, 
     'помещение': {'просторное', 'загородное'}, 
     'доп факты': {'просторный двор'}, 
     'нужен ли опыт владельцу?': 1, 
     'подходит ли для семьи с детьми?': 1},

    {'id': 2, 
     'название': 'Самоедская лайка', 
     '№ группы': 5, 
     '№ секции': 1, 
     'название секции': 'Северные ездовые собаки', 
     'страна происхождения': {'Россия'}, 
     'специализация': {'ездовая собака', 'охотничья собака (на мелкую дичь)'}, 
     'средний рост': 51, 
     'средний вес': 26.5, 
     'средняя продолжительность жизни': 12, 
     'обучаемость': 'средняя', 
     'активность': 'выше среднего', 
     'длина шерсти': {'длинная'}, 
     'тип волоса': {'двойной'}, 
     'структура': {'плотная'}, 
     'подшёрсток': {'плотный'}, 
     'помещение': {'просторное'}, 
     'доп факты': {'доступ к прогулкам на природе'}, 
     'нужен ли опыт владельцу?': 0, 
     'подходит ли для семьи с детьми?': 1},

    {'id': 3, 
     'название': 'Ротвейлер', 
     '№ группы': 2, 
     '№ секции': 2, 
     'название секции': 'Молоссы', 
     'страна происхождения': {'Германия'}, 
     'специализация': {'служебная собака', 'сторожевая собака', 'собака-поводырь'}, 
     'средний рост': 63.5, 
     'средний вес': 45.5, 
     'средняя продолжительность жизни': 11.5, 
     'обучаемость': 'высокая', 
     'активность': 'выше среднего', 
     'длина шерсти': {'короткая'}, 
     'тип волоса': {'прямой', 'грубый'}, 
     'структура': {'густая'}, 
     'подшёрсток': {'плотный'}, 
     'помещение': {'с укреплённым забором', 'загородное'}, 
     'доп факты': {'просторный двор'}, 
     'нужен ли опыт владельцу?': 1, 
     'подходит ли для семьи с детьми?': 0},

    {'id': 4, 
     'название': 'Немецкая овчарка', 
     '№ группы': 1, 
     '№ секции': 1, 
     'название секции': 'Пастушьи собаки', 
     'страна происхождения': {'Германия'}, 
     'специализация': {'служебная собака'}, 
     'средний рост': 60.5, 
     'средний вес': 38.5, 
     'средняя продолжительность жизни': 12.5, 
     'обучаемость': 'высокая', 
     'активность': 'высокая', 
     'длина шерсти': {'средняя'}, 
     'тип волоса': {'прямой'}, 
     'структура': {'густая'}, 
     'подшёрсток': {'плотный'}, 
     'помещение': {'просторное'}, 
     'доп факты': {'просторный двор'}, 
     'нужен ли опыт владельцу?': 1, 
     'подходит ли для семьи с детьми?': 0},

    {'id': 5, 
     'название': 'Лабрадор-ретривер', 
     '№ группы': 8, 
     '№ секции': 1, 
     'название секции': 'Ретриверы', 
     'страна происхождения': {'Великобритания'}, 
     'специализация': {'охотничья собака (поиск и подача дичи)', 'служебная собака', 'собака-поводырь'}, 
     'средний рост': 55.5, 
     'средний вес': 29.5, 
     'средняя продолжительность жизни': 12.5, 
     'обучаемость': 'высокая', 
     'активность': 'высокая', 
     'длина шерсти': {'короткая'}, 
     'тип волоса': {'прямой', 'волнистый'}, 
     'структура': {'плотная'}, 
     'подшёрсток': {'плотный'}, 
     'помещение': {'просторное'}, 
     'доп факты': {'просторный двор', 'близость к парку или пляжу'}, 
     'нужен ли опыт владельцу?': 0, 
     'подходит ли для семьи с детьми?': 1},

    {'id': 6, 
     'название': 'Золотистый ретривер', 
     '№ группы': 8, 
     '№ секции': 1, 
     'название секции': 'Ретриверы', 
     'страна происхождения': {'Великобритания'}, 
     'специализация': {'охотничья собака (поиск и подача дичи)', 'служебная собака', 'собака-поводырь'}, 
     'средний рост': 56, 
     'средний вес': 31.5, 
     'средняя продолжительность жизни': 13, 
     'обучаемость': 'высокая', 
     'активность': 'средняя', 
     'длина шерсти': {'средняя'}, 
     'тип волоса': {'прямой', 'волнистый'}, 
     'структура': {'густая'}, 
     'подшёрсток': {'плотный'}, 
     'помещение': {'просторное', 'загородное'}, 
     'доп факты': {'просторный двор'}, 
     'нужен ли опыт владельцу?': 0, 
     'подходит ли для семьи с детьми?': 1},

    {'id': 7, 
     'название': 'Доберман', 
     '№ группы': 2, 
     '№ секции': 1, 
     'название секции': 'Пинчеры и шнауцеры', 
     'страна происхождения': {'Германия'}, 
     'специализация': {'служебная собака', 'сторожевая собака'}, 
     'средний рост': 67, 
     'средний вес': 35, 
     'средняя продолжительность жизни': 12.5, 
     'обучаемость': 'высокая', 
     'активность': 'высокая', 
     'длина шерсти': {'короткая'}, 
     'тип волоса': {'гладкий'}, 
     'структура': {'плотная'}, 
     'подшёрсток': {'минимальный'}, 
     'помещение': {'просторное'}, 
     'доп факты': {'закрытый двор'}, 
     'нужен ли опыт владельцу?': 1, 
     'подходит ли для семьи с детьми?': 0},
    
    {'id': 8, 
     'название': 'Алабай', 
     '№ группы': 2, 
     '№ секции': 2, 
     'название секции': 'Молоссы', 
     'страна происхождения': {'регионы Средней Азии'}, 
     'специализация': {'сторожевая собака'}, 
     'средний рост': 67.5, 
     'средний вес': 45, 
     'средняя продолжительность жизни': 13.5, 
     'обучаемость': 'высокая', 
     'активность': 'средняя', 
     'длина шерсти': {'короткая'}, 
     'тип волоса': {'гладкий'}, 
     'структура': {'плотная'}, 
     'подшёрсток': {'минимальный'}, 
     'помещение': {'просторное', 'загородное'}, 
     'доп факты': {'просторный двор'}, 
     'нужен ли опыт владельцу?': 0, 
     'подходит ли для семьи с детьми?': 1},
    
    {'id': 9, 
     'название': 'Тибетский мастиф', 
     '№ группы': 2, 
     '№ секции': 2, 
     'название секции': 'Молоссы', 
     'страна происхождения': {'Тибет'}, 
     'специализация': {'сторожевая собака'}, 
     'средний рост': 63.5, 
     'средний вес': 71, 
     'средняя продолжительность жизни': 10.5, 
     'обучаемость': 'низкая', 
     'активность': 'средняя', 
     'длина шерсти': {'длинная'}, 
     'тип волоса': {'грубый'}, 
     'структура': {'густая'}, 
     'подшёрсток': {'плотный'}, 
     'помещение': {'просторное'}, 
     'доп факты': {'доступ к прогулкам на природе'}, 
     'нужен ли опыт владельцу?': 0, 
     'подходит ли для семьи с детьми?': 1},
    
    {'id': 10, 
     'название': 'Кавказская овчарка', 
     '№ группы': 2, 
     '№ секции': 2, 
     'название секции': 'Молоссы', 
     'страна происхождения': {'страны Кавказского региона'}, 
     'специализация': {'сторожевая собака'}, 
     'средний рост': 68, 
     'средний вес': 57.5, 
     'средняя продолжительность жизни': 10.5, 
     'обучаемость': 'средняя', 
     'активность': 'выше среднего', 
     'длина шерсти': {'длинная'}, 
     'тип волоса': {'грубый'}, 
     'структура': {'густая'}, 
     'подшёрсток': {'плотный'}, 
     'помещение': {'загородное', 'с укреплённым забором'}, 
     'доп факты': {'просторный двор'}, 
     'нужен ли опыт владельцу?': 1, 
     'подходит ли для семьи с детьми?': 0}
]

def filter_data(data, name, country, spec, learning, activity, wool, house, experience, family):
    filtered_data = []
    for item in data:
        if name == 'любая' or name in item['название секции']:
            if country == 'любая' or country in item['страна происхождения']:
                if spec == 'любая' or spec in item['специализация']:
                    if learning == 'любая' or name in item['обучаемость']:
                        if activity == 'любая' or country in item['активность']:
                            if wool == 'любая' or spec in item['длина шерсти']:
                                if house == 'любая' or spec in item['помещение']:
                                    if experience == 'любая' or spec in item['нужен ли опыт владельцу?']:
                                        if family == 'любая' or spec in item['подходит ли для семьи с детьми?']:
                                            filtered_data.append(item)
    return filtered_data

def on_radiobutton_click():
    selected_value = vak.get()
    print("Вы выбрали:", data[int(selected_value)-1]['название'])

    dog = data[int(selected_value)-1]
    n = len(data)
    massiv = [0]*n
    for i in range(n):
        similarity = myMeasure(dog, data[i])
        massiv[i] = similarity
    #print(massiv, "\n")
    
    mass = [0]*n
    for i in range(n):
        mass[i] = [data[i]['название'], massiv[i]]
    #print(mass, "\n")
    
    sorted_mass = sorted(mass, key=lambda x: x[1], reverse=True)
    #print(sorted_mass)

    headers = ["№", "Выбранная порода", "Остальные породы", "Схожесть"]
    table = []
    for i, sublist in enumerate(sorted_mass):
        row = [i+1, data[int(selected_value)-1]['название'], sublist[0], sublist[1]]
        table.append(row)
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print("\n"*3)

def comboboxes(event):
    section_value = dropdown1.get()
    country_value = dropdown2.get()
    spec_value = dropdown3.get()
    learning_value = dropdown4.get()
    activity_value = dropdown5.get()
    wool_value = dropdown6.get()
    house_value = dropdown7.get()
    experience_value = dropdown8.get()
    family_value = dropdown9.get()

    filter = {
        'название секции': 'любая',
        'страна происхождения': 'любая',
        'специализация': 'любая',
        'обучаемость': 'любая',
        'активность': 'любая',
        'длина шерсти': 'любая',
        'помещение': 'любая',
        'нужен ли опыт владельцу?': 'любая',
        'подходит ли для семьи с детьми?': 'любая'
    }

    if section_value:    
        #print('Секция: ', section_value)
        filter['название секции'] = section_value
    
    if country_value:    
        #print('Секция: ', section_value)
        filter['страна происхождения'] = country_value

    if spec_value:    
        #print('Секция: ', section_value)
        filter['специализация'] = spec_value
    
    if learning_value:    
        #print('Секция: ', section_value)
        filter['обучаемость'] = learning_value
    
    if activity_value:    
        #print('Секция: ', section_value)
        filter['активность'] = activity_value

    if wool_value:    
        #print('Секция: ', section_value)
        filter['длина шерсти'] = wool_value
    
    if house_value:    
        #print('Секция: ', section_value)
        filter['помещение'] = house_value

    if experience_value:
        #print('Обучаемость: ', learning_value)
        filter['нужен ли опыт владельцу?'] = experience_value

    if family_value:    
        #print('Секция: ', section_value)
        filter['подходит ли для семьи с детьми?'] = family_value
    print('~', filter) 

def filter():
    section_value = dropdown1.get()
    country_value = dropdown2.get()
    spec_value = dropdown3.get()
    learning_value = dropdown4.get()
    activity_value = dropdown5.get()
    wool_value = dropdown6.get()
    house_value = dropdown7.get()
    experience_value = dropdown8.get()
    family_value = dropdown9.get()

    filtered = []
    filt = filter_data(data, section_value, country_value, spec_value, learning_value, activity_value, wool_value, house_value, experience_value, family_value)
    for item in filt:
        filtered.append(item)
    #print('~~~', filtered)

    selected_value = vak.get()
    n = len(filtered)

    print("\n"*2)
    print("Вы выбрали:", data[int(selected_value)-1]['название'])
    dog = data[int(selected_value)-1]
        
    massiv = [0]*n
    for i in range(n):
        similarity = myMeasure(dog, filtered[i])
        massiv[i] = similarity
    #print(massiv, "\n")
        
    mass = [0]*n
    for i in range(n):
        mass[i] = [filtered[i]['название'], massiv[i]]
    #print(mass, "\n")
        
    sorted_mass = sorted(mass, key=lambda x: x[1], reverse=True)
    #print(sorted_mass)

    headers = ["№", "Выбранная порода", "Остальные породы", "Схожесть"]
    table = []
    for i, sublist in enumerate(sorted_mass):
        row = [i+1, data[int(selected_value)-1]['название'], sublist[0], sublist[1]]
        table.append(row)
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print("\n"*3)

section = ['любая']
for item in data:
    if item['название секции'] not in section:
        section.append(item['название секции'])

country = ['любая'] 
for item in data: 
    countries = item['страна происхождения']
    for c in countries:
        if c not in country:
            country.append(c)

specialisazion = ['любая'] 
for item in data: 
    spec = item['специализация']
    for c in spec:
        if c not in specialisazion:
            specialisazion.append(c)

learning = ['не выбрано']
for item in data:
    if item['обучаемость'] not in learning:
        learning.append(item['обучаемость'])

activity = ['не выбрано']
for item in data:
    if item['активность'] not in activity:
        activity.append(item['активность'])

wool = ['не выбрано'] 
for item in data: 
    wools = item['длина шерсти']
    for c in wools:
        if c not in wool:
            wool.append(c)

house = ['не выбрано'] 
for item in data: 
    houses = item['помещение']
    for c in houses:
        if c not in house:
            house.append(c)

experience = ['не выбрано']
for item in data:
    if item['нужен ли опыт владельцу?'] not in experience:
        experience.append(item['нужен ли опыт владельцу?'])

family = ['не выбрано']
for item in data:
    if item['подходит ли для семьи с детьми?'] not in family:
        family.append(item['подходит ли для семьи с детьми?'])

root = tk.Tk()
vak = tk.StringVar()

root.title("Породы собак")
root.geometry('430x490') 

n = len(data)

text = [0]*n
var = [0]*n

for i in range(n):
    text[i]=data[i]['название']
    var[i]=data[i]['id']

for i in range(n):
    radio_button = Radiobutton(root, text=text[i], variable=vak, value=var[i], command=on_radiobutton_click) 
    radio_button.pack()

lbl = ttk.Label(root, text = "Выберите значение в каждой строке, либо выберите 'любая'")
lbl.pack()

label1 = ttk.Label(root, text = "Фильтр по секции: ")
label1.pack()
dropdown1 = ttk.Combobox(root, values=section)
dropdown1.pack()

label2 = ttk.Label(root, text = "Фильтр по стране: ")
label2.pack()
dropdown2 = ttk.Combobox(root, values=country)
dropdown2.pack()

label3 = ttk.Label(root, text = "Фильтр по специализации: ")
label3.pack()
dropdown3 = ttk.Combobox(root, values=specialisazion)
dropdown3.pack()

label4 = ttk.Label(root, text = "Фильтр по обучаемости: ")
label4.pack()
dropdown4 = ttk.Combobox(root, values=learning)
dropdown4.pack()

label5 = ttk.Label(root, text = "Фильтр по активности: ")
label5.pack()
dropdown5 = ttk.Combobox(root, values=activity)
dropdown5.pack()

label6 = ttk.Label(root, text = "Фильтр по длине шерсти: ")
label6.pack()
dropdown6 = ttk.Combobox(root, values=wool)
dropdown6.pack()

label7 = ttk.Label(root, text = "Фильтр по дому: ")
label7.pack()
dropdown7 = ttk.Combobox(root, values=house)
dropdown7.pack()

label8 = ttk.Label(root, text = "Фильтр по опыту: ")
label8.pack()
dropdown8 = ttk.Combobox(root, values=experience)
dropdown8.pack()

label9 = ttk.Label(root, text = "Фильтр по семье: ")
label9.pack()
dropdown9 = ttk.Combobox(root, values=family)
dropdown9.pack()

result_button = ttk.Button(root, text="Фильтровать", command=filter)
result_button.pack()

#label = ttk.Label(root, text = "Выбранные породы собак: ")
#label.pack()

# Связываем событие выбора значения с функцией обработчиком
dropdown1.bind("<<ComboboxSelected>>", comboboxes)
dropdown2.bind("<<ComboboxSelected>>", comboboxes)
dropdown3.bind("<<ComboboxSelected>>", comboboxes)
dropdown4.bind("<<ComboboxSelected>>", comboboxes)
dropdown5.bind("<<ComboboxSelected>>", comboboxes)
dropdown6.bind("<<ComboboxSelected>>", comboboxes)
dropdown7.bind("<<ComboboxSelected>>", comboboxes)
dropdown8.bind("<<ComboboxSelected>>", comboboxes)
dropdown9.bind("<<ComboboxSelected>>", comboboxes)

root.mainloop()
