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

def on_checkbox_click2():
    n = len(data)
    selected_vars = []
    ind = 0
    for i in range(n):
        if var2[i].get() == 1:
            ind = i
            selected_vars.append(ind)
            ind = 0
    print(selected_vars)

def show_result2():
    n = len(data)
    selected_vars = []
    ind = 0
    for i in range(n):
        if var2[i].get() == 1:
            ind = i
            selected_vars.append(ind)
            ind = 0
    m = len(selected_vars)
    
    if m == 0:
        messagebox.showinfo("GUI Python", "Выберите хотя бы одну породу")
    else:
        #массив выбранных пород (номер в списке + название)
        data_for_sv = [0]*m
        #ind = [0]*m
        for i in range(m):
            data_for_sv[i] = [data[selected_vars[i]]['id'] - 1, str(data[selected_vars[i]]['название'])]
        print("Вам нравятся: ", data_for_sv)
        
        #массив словарей с выбранными породами и их хар-ками из data
        selected_breeds = [0]*m
        for i in range(n):
            name = data[i]['название']
            #print(name)
            for j in range(m):
                if name in data_for_sv[j][1]:
                    #print(data_for_sv[j][1])
                    selected_breeds[j] = data[i]
                    #print(selected_breeds[j])
                    continue
        #print(selected_breeds)
        
        massiv = []
        for j in range(m):
            dog = selected_breeds[j]
            #print(selected_breeds[j]['название'])
            for i in range(n):
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
        
        value_to_remove = 'Самоедская лайка'

        i = 0
        while i < len(result):
            if result[i][0] == value_to_remove:
                del result[i]
            else:
                i += 1
        #print(result)
        print("\n"*3)

root = tk.Tk()
vak = tk.StringVar()
vak_check = tk.IntVar()

root.title("Породы собак") 
root.geometry('450x250')

#Создание виджета Notebook
notebook = ttk.Notebook(root)

#Создание вкладок
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1, text='Первая')
notebook.add(tab2, text='Вторая')
notebook.add(tab3, text='Третья')

#tab1.pack(fill="both", expand=True)

# Create a Scrollbar
scrollbar1 = ttk.Scrollbar(tab1)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar2 = ttk.Scrollbar(tab2)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar3 = ttk.Scrollbar(tab3)
scrollbar3.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Canvas
canvas1 = tk.Canvas(tab1, yscrollcommand=scrollbar1.set)
canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

canvas2 = tk.Canvas(tab2, yscrollcommand=scrollbar2.set)
canvas2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

canvas3 = tk.Canvas(tab3, yscrollcommand=scrollbar3.set)
canvas3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configure the Scrollbar to work with the Canvas
scrollbar1.config(command=canvas1.yview)
scrollbar2.config(command=canvas2.yview)
scrollbar3.config(command=canvas3.yview)

# Create a Frame inside the Canvas
frame1 = ttk.Frame(canvas1)
canvas1.create_window((0, 0), window=frame1, anchor=tk.NW)

frame2 = ttk.Frame(canvas2)
canvas2.create_window((0, 0), window=frame2, anchor=tk.NW)

frame3 = ttk.Frame(canvas3)
canvas3.create_window((0, 0), window=frame3, anchor=tk.NW)

# Create Radiobuttons inside the Frame
#ПЕРВАЯ ВКЛАДКА
lbl1 = ttk.Label(frame1, text='(На входе 1 лайк)') 
label1 = ttk.Label(frame1, text="Выберите одну из следующих пород собак:")
lbl1.pack() 
label1.pack()

n = len(data)

text = [0]*n
var = [0]*n

for i in range(n):
    text[i]=data[i]['название']
    var[i]=data[i]['id']

for i in range(n):
    radio_button = ttk.Radiobutton(frame1, text=text[i], variable=vak, value=var[i], command=on_radiobutton_click)
    radio_button.pack()

#ВТОРАЯ ВКЛАДКА
lbl2 = ttk.Label(frame2, text='(На входе n штук лайков)') 
label2 = ttk.Label(frame2, text="Выберите не менее одной из следующих пород собак:")
lbl2.pack() 
label2.pack()

var2 = [0]*n

for i in range(n):
    var2[i] = tk.IntVar()

for i in range(n):
    checkbox = ttk.Checkbutton(frame2, text=text[i], variable=var2[i], command=on_checkbox_click2) 
    checkbox.pack()

result_button = ttk.Button(frame2, text="Покажи результат", command=show_result2)
result_button.pack()

#ТРЕТЬЯ ВКЛАДКА
lbl3 = ttk.Label(frame3, text='(На входе n штук лайков и w дизлайков)') 
label31 = ttk.Label(frame3, text="Выберите породы собак, которые вам нравятся (не менее одной):")
lbl3.pack() 
label31.pack()

var31 = [0]*n
for i in range(n):
    var31[i] = tk.IntVar()

for i in range(n):
    checkbox31 = ttk.Checkbutton(frame3, text=text[i], variable=var31[i], command=on_checkbox_click31) 
    checkbox31.pack()

label32 = ttk.Label(frame3, text="Выберите породы собак, которые вам НЕ нравятся (можно не выбирать):")
label32.pack()

var32 = [0]*n
for i in range(n):
    var32[i] = tk.IntVar()

for i in range(n):
    checkbox32 = ttk.Checkbutton(frame3, text=text[i], variable=var32[i], command=on_checkbox_click32) 
    checkbox32.pack()

result_button3 = ttk.Button(frame3, text="Покажи результат", command=show_result3)
result_button3.pack()

# Update the Canvas scroll region
frame1.update_idletasks()
canvas1.config(scrollregion=canvas1.bbox("all"))

frame2.update_idletasks()
canvas2.config(scrollregion=canvas2.bbox("all"))

frame3.update_idletasks()
canvas3.config(scrollregion=canvas3.bbox("all"))

notebook.pack(expand=1, fill='both')
root.mainloop()
