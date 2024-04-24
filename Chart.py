import matplotlib.pyplot as plt
import numpy as np

## Создание шрифтов для обозначений
font1 = {'family':'serif','color':'green','size':15}

## Создание графика
y = np.array([25, 14, 4, 7, 9, 11, 13, 17])
mylabels = ["Кабачки 25%", "Другое 14%", "Лук 4%", "Картофель 7%", "Авокадо 9%", "Огурцы 11%", "Баклажаны 13%", "Помидоры 17%"]

## Выделение "Другого"
myexplode = [0, 0.07, 0, 0, 0, 0, 0, 0]

## Назначение цветов
mycolors = ["blue", "brown", "darkblue", "green", "blue", "yellow", "gray", "orange"]

## Создание обозначений по x и по y
plt.title("Продажи овощей", fontdict = font1)

## Отметка графика
plt.pie(y, labels = mylabels, explode = myexplode, colors = mycolors)

## Показ легенды диаграммы
plt.legend(title = "Все овощи:")

## Показ графика
plt.show()