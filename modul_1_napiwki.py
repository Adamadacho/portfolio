# -*- coding: utf-8 -*-
"""Modul_1_Napiwki.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VgqRAoHaZ2ncpgGbGyRgj0ctcmjWdF8h
"""

import pandas as pd
import matplotlib.pyplot as plt

url = "https://github.com/mwaskom/seaborn-data/raw/master/tips.csv"
data = pd.read_csv(url)

print(data.head())
print(data.info())

average_tip = data['tip'].mean()
print(f"Average tip is {average_tip:.2f} USD")

average_tip_by_gender = data.groupby("sex")['tip'].mean()

for gender, average_tip in average_tip_by_gender.items():
  print(f"Average tip for {gender}: {average_tip:.2f} USD")

median_tip = data['tip'].median()
print(f'Mediana wynosi: {median_tip} USD')

deviation = data['tip'].std()
print(f'Odchylenie standardowe wynosi: {deviation: .2f} USD')

data.boxplot(column='tip', by='sex')
plt.title('rozkład napiwków według płci')
plt.suptitle('test')
plt.xlabel("płeć")
plt.ylabel('napiwek [USD]')
plt.show()

avg_tips_by_day = data. groupby('day')["tip"].mean()

avg_tips_by_day.plot(kind='bar', title="Średnie napiwki wg dnia", ylabel="Średni napiwek (USD)", xlabel="Dzień")
plt.show()