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

def filter_data(data, name, country, spec):
    filtered_data = []
    for item in data:
        if name == 'любая' or name in item['название секции']:
            if country == 'любая' or country in item['страна происхождения']:
                if spec == 'любая' or spec in item['специализация']:
                    filtered_data.append(item)
    return filtered_data

def on_checkbox_click31():
    n = len(data)
    selected_vars = []
    ind = 0
    for i in range(n):
        if var31[i].get() == 1:
            ind = i
            selected_vars.append(ind)
            ind = 0
    print("like: ", selected_vars)

def on_checkbox_click32():
    n = len(data)
    selected_vars = []
    ind = 0
    for i in range(n):
        if var32[i].get() == 1:
            ind = i
            selected_vars.append(ind)
            ind = 0
    print("dislike: ", selected_vars)

def show_result3():
    n = len(data)
    selected_vars_like = []
    ind_like = 0
    for i in range(n):
        if var31[i].get() == 1:
            ind_like = i
            selected_vars_like.append(ind_like)
            ind_like = 0
    m_like = len(selected_vars_like)
    #print(m_like)
    
    selected_vars_dislike = []
    ind_dislike = 0
    for i in range(n):
        if var32[i].get() == 1:
            ind_dislike = i
            selected_vars_dislike.append(ind_dislike)
            ind_dislike = 0
    m_dislike = len(selected_vars_dislike)
    #print(m_dislike)
    
    if m_like == 0:
        messagebox.showinfo("GUI Python", "Выберите хотя бы одну породу, которая вам нравится")
    else:
        #массив выбранных пород (номер в списке + название)
        data_for_sv_like = [0]*m_like
        #ind = [0]*m_like
        for i in range(m_like):
            data_for_sv_like[i] = [data[selected_vars_like[i]]['id'] - 1, str(data[selected_vars_like[i]]['название'])]
        print("Вам нравятся: ", data_for_sv_like)
        
        data_for_sv_dislike = [0]*m_dislike
        #ind = [0]*m_like
        for i in range(m_dislike):
            data_for_sv_dislike[i] = [data[selected_vars_dislike[i]]['id'] - 1, str(data[selected_vars_dislike[i]]['название'])]
        print("Вам НЕ нравятся: ", data_for_sv_dislike)

        #массив словарей с выбранными породами и их хар-ками из data
        selected_breeds = [0]*m_like
        for i in range(n):
            name = data[i]['название']
            #print(name)
            for j in range(m_like):
                if name in data_for_sv_like[j][1]:
                    #print(data_for_sv[j][1])
                    selected_breeds[j] = data[i]
                    #print(selected_breeds[j])
                    continue
        #print(selected_breeds)
        
        massiv = []
        for j in range(m_like):
            dog = selected_breeds[j]
            #print(selected_breeds[j]['название'])
            for i in range(len(data)):
                if data[i]['название'] in [item[1] for item in data_for_sv_dislike]:
                    continue
                similarity = myMeasure(dog, data[i])
                massiv.append([data[i]['название'], similarity])
        #print(massiv, "\n") 

        sorted_mass = sorted(massiv, key=lambda x: x[1], reverse=True)
        #print(sorted_mass)

        max_values = {}
        for item in sorted_mass:
            key = item[0]
            value = item[1]
            if key in max_values and value > max_values[key]:
                max_values[key] = value
            elif key not in max_values:
                max_values[key] = value
        
        result = [[key, value] for key, value in max_values.items()]
        #print(result)

        headers = ["№", "Породы", "Схожесть"]
        table = []
        for i, sublist in enumerate(result):
            row = [i+1, sublist[0], sublist[1]]
            table.append(row)
        print(tabulate(table, headers=headers, tablefmt="grid"))
        print("\n"*3)

def comboboxes(event):
    section_value = dropdown1.get()
    country_value = dropdown2.get()
    spec_value = dropdown3.get()

    filter = {
        'название секции': 'любая',
        'страна происхождения': 'любая',
        'специализация': 'любая'
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
    print('~', filter) 

def filter():
    section_value = dropdown1.get()
    country_value = dropdown2.get()
    spec_value = dropdown3.get()

    filtered = []
    filt = filter_data(data, section_value, country_value, spec_value)
    for item in filt:
        filtered.append(item)
    #print('~~~', filtered)

    n = len(data)
    selected_vars_like = []
    ind_like = 0
    for i in range(n):
        if var31[i].get() == 1:
            ind_like = i
            selected_vars_like.append(ind_like)
            ind_like = 0
    m_like = len(selected_vars_like)
    #print(m_like)
    
    selected_vars_dislike = []
    ind_dislike = 0
    for i in range(n):
        if var32[i].get() == 1:
            ind_dislike = i
            selected_vars_dislike.append(ind_dislike)
            ind_dislike = 0
    m_dislike = len(selected_vars_dislike)
    #print(m_dislike)
    
    if m_like == 0:
        messagebox.showinfo("GUI Python", "Выберите хотя бы одну породу, которая вам нравится")
    else:
        #массив выбранных пород (номер в списке + название)
        data_for_sv_like = [0]*m_like
        #ind = [0]*m_like
        for i in range(m_like):
            data_for_sv_like[i] = [data[selected_vars_like[i]]['id'] - 1, str(data[selected_vars_like[i]]['название'])]
        print("Вам нравятся: ", data_for_sv_like)
        
        data_for_sv_dislike = [0]*m_dislike
        #ind = [0]*m_like
        for i in range(m_dislike):
            data_for_sv_dislike[i] = [data[selected_vars_dislike[i]]['id'] - 1, str(data[selected_vars_dislike[i]]['название'])]
        print("Вам НЕ нравятся: ", data_for_sv_dislike)

        #массив словарей с выбранными породами и их хар-ками из data
        selected_breeds = [0]*m_like
        for i in range(n):
            name = data[i]['название']
            #print(name)
            for j in range(m_like):
                if name in data_for_sv_like[j][1]:
                    #print(data_for_sv[j][1])
                    selected_breeds[j] = data[i]
                    #print(selected_breeds[j])
                    continue
        #print(selected_breeds)
        
        massiv = []
        for j in range(m_like):
            dog = selected_breeds[j]
            #print(selected_breeds[j]['название'])
            for i in range(len(filtered)):
                if filtered[i]['название'] in [item[1] for item in data_for_sv_dislike]:
                    continue
                similarity = myMeasure(dog, filtered[i])
                massiv.append([filtered[i]['название'], similarity])
        #print(massiv, "\n") 

        sorted_mass = sorted(massiv, key=lambda x: x[1], reverse=True)
        #print(sorted_mass)

        max_values = {}
        for item in sorted_mass:
            key = item[0]
            value = item[1]
            if key in max_values and value > max_values[key]:
                max_values[key] = value
            elif key not in max_values:
                max_values[key] = value
        
        result = [[key, value] for key, value in max_values.items()]
        #print(result)

        headers = ["№", "Породы", "Схожесть"]
        table = []
        for i, sublist in enumerate(result):
            row = [i+1, sublist[0], sublist[1]]
            table.append(row)
        print(tabulate(table, headers=headers, tablefmt="grid"))

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

root = tk.Tk()
vak = tk.StringVar()

root.title("Породы собак")
root.geometry('430x690') 

n = len(data)

lbl1 = ttk.Label(root, text="Выберите породы собак, которые вам нравятся (не менее одной):")
lbl1.pack()

text = [0]*n
var31 = [0]*n

for i in range(n):
    text [i] = data[i]['название']
    var31[i] = tk.IntVar()

for i in range(n):
    checkbox31 = ttk.Checkbutton(root, text=text[i], variable=var31[i], command=on_checkbox_click31) 
    checkbox31.pack()

lbl2 = ttk.Label(root, text="Выберите породы собак, которые вам НЕ нравятся (можно не выбирать):")
lbl2.pack()

var32 = [0]*n
for i in range(n):
    var32[i] = tk.IntVar()

for i in range(n):
    checkbox32 = ttk.Checkbutton(root, text=text[i], variable=var32[i], command=on_checkbox_click32) 
    checkbox32.pack()

result_button3 = ttk.Button(root, text="Покажи результат", command=show_result3)
result_button3.pack()

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

result_button = ttk.Button(root, text="Фильтровать", command=filter)
result_button.pack()

#label = ttk.Label(root, text = "Выбранные породы собак: ")
#label.pack()

# Связываем событие выбора значения с функцией обработчиком
dropdown1.bind("<<ComboboxSelected>>", comboboxes)
dropdown2.bind("<<ComboboxSelected>>", comboboxes)
dropdown3.bind("<<ComboboxSelected>>", comboboxes)

root.mainloop()
