4
#5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099

import math
print('Введите ккординаты двух точек на плоскости, и я определю расстояние между ними')
x1 = float(input('Координата x первой точки: '))
y1 = float(input('Координата y первой точки: '))
x2 = float(input('Координата x второй точки: '))
y2 = float(input('Координата y второй точки: '))
dist = round(math.sqrt((x2-x1)**2+(y2-y1)**2),3)
print('Растояние между точками равно', dist)