from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox
from tkinter.ttk import Radiobutton
import numpy as np
import pandas as pd
from tabulate import tabulate
from measure import myMeasure

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
        """
        value_to_remove = 'Самоедская лайка'

        i = 0
        while i < len(result):
            if result[i][0] == value_to_remove:
                del result[i]
            else:
                i += 1
        #print(result)
        """
        print("\n"*3)
        
window = Tk() 
vak = StringVar()
vak_check = IntVar()

window.title("Породы собак") 
window.geometry('430x690') 

tab_control = ttk.Notebook(window) 

tab1 = ttk.Frame(tab_control) 
tab2 = ttk.Frame(tab_control) 
tab3 = ttk.Frame(tab_control) 

tab_control.add(tab1, text='Первая') 
tab_control.add(tab2, text='Вторая') 
tab_control.add(tab3, text='Третья') 

#ПЕРВАЯ ВКЛАДКА
lbl1 = Label(tab1, text='(На входе 1 лайк)') 
label1 = Label(tab1, text="Выберите одну из следующих пород собак:")
lbl1.grid(column=0, row=0) 
label1.grid(column=0, row=1)

n = len(data)

row = 2
text = [0]*n
var = [0]*n

for i in range(n):
    text[i]=data[i]['название']
    var[i]=data[i]['id']

for i in range(n):
    radio_button = Radiobutton(tab1, text=text[i], variable=vak, value=var[i], command=on_radiobutton_click) 
    radio_button.grid(column=0, row=row)
    row += 1 

#ВТОРАЯ ВКЛАДКА
lbl2 = Label(tab2, text='(На входе n штук лайков)') 
label2 = Label(tab2, text="Выберите не менее одной из следующих пород собак:")
lbl2.grid(column=0, row=0) 
label2.grid(column=0, row=1)

var2 = [0]*n
row = 2
for i in range(n):
    var2[i] = IntVar()

for i in range(n):
    checkbox = Checkbutton(tab2, text=text[i], variable=var2[i], command=on_checkbox_click2) 
    checkbox.grid(column=0, row=row)
    row += 1 

result_button = Button(tab2, text="Покажи результат", command=show_result2)
result_button.grid(column=0, row=row)

#ТРЕТЬЯ ВКЛАДКА
lbl3 = Label(tab3, text='(На входе n штук лайков и w дизлайков)') 
label31 = Label(tab3, text="Выберите породы собак, которые вам нравятся (не менее одной):")
lbl3.grid(column=0, row=0) 
label31.grid(column=0, row=1)

var31 = [0]*n
row = 2
for i in range(n):
    var31[i] = IntVar()

for i in range(n):
    checkbox31 = Checkbutton(tab3, text=text[i], variable=var31[i], command=on_checkbox_click31) 
    checkbox31.grid(column=0, row=row)
    row += 1 

label32 = Label(tab3, text="Выберите породы собак, которые вам НЕ нравятся (можно не выбирать):")
label32.grid(column=0, row=row)
row += 1

var32 = [0]*n
for i in range(n):
    var32[i] = IntVar()

for i in range(n):
    checkbox32 = Checkbutton(tab3, text=text[i], variable=var32[i], command=on_checkbox_click32) 
    checkbox32.grid(column=0, row=row)
    row += 1 

result_button3 = Button(tab3, text="Покажи результат", command=show_result3)
result_button3.grid(column=0, row=row)

tab_control.pack(expand=1, fill='both') 

window.mainloop()
