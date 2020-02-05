#!/usr/bin/python
# -*- coding: utf-8 -*-

#Задача с ip адресами
#Есть файл со строками (https://yadi.sk/d/u6AOqGqKozTrpw) вида :
#<host>\t<ip>\t<page>\n
#Нужно вывести 5 айпи-адресов, которые встречаются чаще других.

import pandas as pd

df = pd.read_csv('taskIP/hits.txt', sep='\t', names=['host','ip','page'])
print(df.ip.value_counts().head(5))