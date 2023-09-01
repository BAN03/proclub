#!/usr/bin/python3

valor_a = int(input())
valor_b = int(input())
valor_c = int(input())

area_triangulo = (valor_a - valor_c) * valor_b / 2
area_rectangulo = valor_b * valor_c
area_total = int(area_triangulo + area_rectangulo)

print(area_total, end='')