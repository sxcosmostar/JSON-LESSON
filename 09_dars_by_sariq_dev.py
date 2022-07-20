# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 14:29:36 2022

@author: user
"""

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print('Salom', mehmon)
#     print('Hayr', mehmon)
#     print(f"Hurmatli {mehmon} sizni 20 Dekabr kuni naxorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi!!!\n")

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son ** 2} ga teng")

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son ** 2)
    
# print('Sonlar: ', sonlar)
# print('Sonlar kvadrati: ', sonlar_kvadrati)

dostlar = []
print('5ta eng yaqin do\'stingizni kiriting' )
for n in range(5):
    dostlar.append(input(f"{n+1}-do'tingizni ismini kiriting: "))
    
print(dostlar)